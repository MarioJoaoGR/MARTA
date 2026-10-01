"""Linux job memory diagnostics, without dependencies or inference calls.

Read only this Slurm job's cgroups/processes. Never record command lines or
environment variables: the cluster account is shared. RSS sums double-count
shared pages; cgroup usage is the authoritative aggregate when available.
"""
# Runs with the compute node's Python 3.6 as well as the container's newer Python.
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path, PurePosixPath
import re
import signal
import threading


def read(path: Path) -> str:
    try:
        return path.read_text()
    except (OSError, UnicodeError):
        return ""


def process_table(proc: Path) -> dict:
    result = {}
    for directory in proc.iterdir():
        if not directory.name.isdigit():
            continue
        fields = dict(line.split(":", 1) for line in read(directory / "status").splitlines()
                      if ":" in line)
        if "PPid" not in fields:
            continue
        item = {"pid": int(directory.name), "ppid": int(fields["PPid"]),
                "name": fields.get("Name", "").strip(),
                "state": (fields.get("State", "").split() or ["?"])[0]}
        for source, dest in (("VmRSS", "rss_bytes"), ("VmSize", "virtual_bytes")):
            value = fields.get(source, "").split()
            item[dest] = int(value[0]) * 1024 if value else 0
        item["cgroups"] = read(directory / "cgroup")
        result[item["pid"]] = item
    return result


def in_job(cgroups: str, job_id: str) -> bool:
    return bool(re.search(r"(?:^|/)job_" + re.escape(job_id) + r"(?:/|$)", cgroups,
                          flags=re.MULTILINE))


def select_processes(table: dict, root_pid: int, job_id: str) -> list:
    selected = {pid for pid, item in table.items() if in_job(item["cgroups"], job_id)}
    # Fallback for systems hiding cgroups; descendants never include other jobs.
    descendants = {root_pid} if root_pid in table else set()
    while True:
        children = {pid for pid, item in table.items() if item["ppid"] in descendants}
        if children <= descendants:
            break
        descendants.update(children)
    selected.update(descendants)
    return sorted(({k: v for k, v in table[pid].items() if k != "cgroups"}
                   for pid in selected), key=lambda item: (-item["rss_bytes"], item["pid"]))


def unescape_mount(value: str) -> str:
    return re.sub(r"\\([0-7]{3})", lambda m: chr(int(m[1], 8)), value)


def memory_groups(cgroups: str, mountinfo: str, job_id: str) -> list:
    """Resolve v1/v2 memory mounts, including a mount with a non-root origin."""
    paths = []
    for line in cgroups.splitlines():
        parts = line.split(":", 2)
        if len(parts) == 3 and (parts[1] == "" or "memory" in parts[1].split(",")):
            paths.append((2 if parts[1] == "" else 1, PurePosixPath(parts[2])))
    result = []
    for line in mountinfo.splitlines():
        left, separator, right = line.partition(" - ")
        before, after = left.split(), right.split()
        if not separator or len(before) < 5 or len(after) < 3:
            continue
        for version, group in paths:
            if after[0] != ("cgroup2" if version == 2 else "cgroup"):
                continue
            if version == 1 and "memory" not in after[2].split(","):
                continue
            mount_root = PurePosixPath(unescape_mount(before[3]))
            candidates = [group]
            # Job aggregate includes subprocesses from every step, not other jobs.
            for parent in group.parents:
                if parent.name == "job_" + job_id:
                    candidates.insert(0, parent)
                    break
            for candidate in candidates:
                try:
                    relative = candidate.relative_to(mount_root)
                except ValueError:
                    continue
                if not in_job(str(candidate), job_id):
                    continue
                item = (version, Path(unescape_mount(before[4])) / str(relative), str(candidate))
                if item not in result:
                    result.append(item)
    return result


def counters(text: str) -> dict:
    result = {}
    for line in text.splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[1].isdigit():
            result[parts[0]] = int(parts[1])
    return result


def group_usage(version: int, directory: Path, group: str) -> dict:
    item = {"version": version, "group": group}
    files = ({"usage_bytes": "memory.current", "limit_bytes": "memory.max",
              "peak_bytes": "memory.peak"} if version == 2 else
             {"usage_bytes": "memory.usage_in_bytes", "limit_bytes": "memory.limit_in_bytes",
              "peak_bytes": "memory.max_usage_in_bytes"})
    for name, file in files.items():
        value = read(directory / file).strip()
        item[name] = int(value) if value.isdigit() else None
    item["events"] = counters(read(directory / ("memory.events" if version == 2
                                                   else "memory.oom_control")))
    item["stat"] = counters(read(directory / "memory.stat"))
    return item


def snapshot(proc: Path, root_pid: int, job_id: str) -> dict:
    table = process_table(proc)
    processes = select_processes(table, root_pid, job_id)
    groups = memory_groups(table.get(root_pid, {}).get("cgroups", ""),
                           read(proc / "self/mountinfo"), job_id)
    return {"time": datetime.now(timezone.utc).isoformat(), "job_id": job_id,
            "root_alive": root_pid in table and table[root_pid]["state"] != "Z",
            "rss_sum_bytes_shared_pages_counted_per_process": sum(p["rss_bytes"] for p in processes),
            "processes": processes, "memory_cgroups": [group_usage(*g) for g in groups]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--job-id", required=True)
    parser.add_argument("--root-pid", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--interval", type=float, default=30)
    args = parser.parse_args()
    if args.interval <= 0 or not args.job_id.isdigit():
        parser.error("interval must be positive and job-id numeric")
    stop = threading.Event()
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda *_: stop.set())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a", buffering=1) as output:
        while not stop.is_set():
            item = snapshot(Path("/proc"), args.root_pid, args.job_id)
            output.write(json.dumps(item) + "\n")
            if not item["root_alive"]:
                break
            stop.wait(args.interval)


if __name__ == "__main__":
    main()
