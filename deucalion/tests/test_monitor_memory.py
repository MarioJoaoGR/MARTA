import ast
import json
from pathlib import Path
import signal
import subprocess
import sys
import time

import pytest

from deucalion import monitor_memory as monitor
from benchmark.xrepotest.tests.test_cluster import fake_cluster


def test_host_monitor_keeps_python36_syntax_and_no_future_annotations():
    source = Path(monitor.__file__).read_text()
    tree = ast.parse(source, feature_version=(3, 6))
    assert not any(isinstance(node, ast.ImportFrom) and node.module == "__future__"
                   and any(alias.name == "annotations" for alias in node.names)
                   for node in ast.walk(tree))


def process(proc, pid, ppid, *, group="", rss=12):
    directory = proc / str(pid)
    directory.mkdir(parents=True)
    (directory / "status").write_text(
        f"Name:\tworker\nState:\tS (sleeping)\nPPid:\t{ppid}\n"
        f"VmRSS:\t{rss} kB\nVmSize:\t40 kB\n")
    (directory / "cgroup").write_text(group)
    # These must never be read or exported.
    (directory / "cmdline").write_text("PRIVATE_ARGUMENT")
    (directory / "environ").write_text("PRIVATE_TOKEN")


def test_snapshot_isolates_job_and_uses_descendants_without_cgroups(tmp_path):
    proc = tmp_path / "proc"
    process(proc, 100, 1, group="0::/slurm/job_123/step_batch\n")
    process(proc, 101, 100)
    process(proc, 102, 101)
    process(proc, 103, 1, group="0::/slurm/job_123/step_0\n")
    process(proc, 104, 1, group="0::/slurm/job_1234/step_batch\n")
    process(proc, 105, 1, group="0::/slurm/job_999/step_batch\n")
    process(proc, 106, 1)
    result = monitor.snapshot(proc, 100, "123")
    assert {p["pid"] for p in result["processes"]} == {100, 101, 102, 103}
    assert result["root_alive"]
    assert result["rss_sum_bytes_shared_pages_counted_per_process"] == 4 * 12 * 1024
    assert "PRIVATE" not in json.dumps(result)
    assert not monitor.snapshot(proc, 777, "123")["root_alive"]


@pytest.mark.parametrize("version", [1, 2])
def test_memory_mount_job_aggregate_and_step_are_both_read(tmp_path, version):
    mount = tmp_path / "memory"
    job = mount / "slurm/job_123"
    step = job / "step_batch"
    step.mkdir(parents=True)
    proc = tmp_path / "proc"
    proc.joinpath("self").mkdir(parents=True)
    if version == 1:
        groups = "4:cpu:/other\n5:memory:/slurm/job_123/step_batch\n"
        (proc / "self/mountinfo").write_text(
            f"30 20 0:30 / {mount} rw - cgroup memory rw,memory\n")
        files = {"memory.usage_in_bytes": "4096", "memory.limit_in_bytes": "8192",
                 "memory.max_usage_in_bytes": "6000", "memory.oom_control": "oom_kill 1\n"}
    else:
        groups = "0::/slurm/job_123/step_batch\n"
        (proc / "self/mountinfo").write_text(
            f"30 20 0:30 / {mount} rw - cgroup2 cgroup rw\n")
        files = {"memory.current": "4096", "memory.max": "8192",
                 "memory.peak": "6000", "memory.events": "oom 2\noom_kill 1\n"}
    for directory in (job, step):
        for file, value in files.items():
            (directory / file).write_text(value)
        (directory / "memory.stat").write_text("anon 2048\nfile 1024\n")
    process(proc, 100, 1, group=groups)
    result = monitor.snapshot(proc, 100, "123")
    stats = result["memory_cgroups"]
    assert [s["group"] for s in stats] == ["/slurm/job_123", "/slurm/job_123/step_batch"]
    assert stats[0]["usage_bytes"] == 4096
    assert stats[0]["limit_bytes"] == 8192
    assert stats[0]["peak_bytes"] == 6000
    assert stats[0]["events"]["oom_kill"] == 1
    assert stats[0]["stat"]["file"] == 1024


def test_mount_origin_escaping_and_no_unrelated_cgroup_measurement(tmp_path):
    mount = tmp_path / "with space"
    escaped = str(mount).replace(" ", r"\040")
    groups = "0::/slurm/job_123/step_batch\n"
    mounts = f"30 20 0:30 /slurm/job_123 {escaped} rw - cgroup2 cgroup rw\n"
    assert monitor.memory_groups(groups, mounts, "123") == [
        (2, mount, "/slurm/job_123"),
        (2, mount / "step_batch", "/slurm/job_123/step_batch")]
    assert monitor.memory_groups(groups, mounts, "456") == []
    assert monitor.memory_groups("", mounts, "123") == []


def test_missing_peak_unlimited_v2_and_exited_process_do_not_crash(tmp_path):
    (tmp_path / "memory.max").write_text("max\n")
    result = monitor.group_usage(2, tmp_path, "/job_123")
    assert result["limit_bytes"] is None and result["peak_bytes"] is None
    assert result["events"] == {}
    process(tmp_path, 100, 1)
    (tmp_path / "101").mkdir()  # A process can exit between listing and status.
    assert list(monitor.process_table(tmp_path)) == [100]


@pytest.mark.parametrize("sig,chains", [(signal.SIGTERM, False), (signal.SIGUSR1, True)])
def test_generation_stops_monitor_and_only_walltime_chains(fake_cluster, sig, chains):
    root, tmp, env = fake_cluster
    monitor_pid = tmp / "monitor.pid"
    shim = tmp / "bin/python3"
    shim.write_text(f'#!{sys.executable}\n'
                    'import os, pathlib, time\n'
                    f'pathlib.Path({str(monitor_pid)!r}).write_text(str(os.getpid()))\n'
                    'time.sleep(60)\n')
    shim.chmod(0o755)
    env["HOLD"] = "1"
    child = subprocess.Popen(["bash", str(root / "deucalion/run_xrepotest_generate_gpu.sh")],
                             env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        for _ in range(100):
            if Path(env["STARTED"]).exists() and monitor_pid.exists():
                break
            if child.poll() is not None:
                pytest.fail(str(child.communicate()))
            time.sleep(.05)
        assert Path(env["STARTED"]).exists() and monitor_pid.exists()
        pid = int(monitor_pid.read_text())
        child.send_signal(sig)
        child.communicate(timeout=10)
        with pytest.raises(ProcessLookupError):
            __import__("os").kill(pid, 0)
        calls = [json.loads(line) for line in (tmp / "calls.jsonl").read_text().splitlines()]
        submissions = [c for c in calls if c[0] == "sbatch"]
        assert bool(submissions) == chains
        if chains:
            assert "--dependency=afterany:123" in submissions[0]
            assert submissions[0][-1] == str(tmp / "MARTA/deucalion/run_xrepotest_generate_gpu.sh")
        assert "#SBATCH --time=08:00:00" in (root / "deucalion/run_xrepotest_generate_gpu.sh").read_text()
    finally:
        if child.poll() is None:
            child.terminate()
            child.communicate(timeout=10)


@pytest.mark.skipif(sys.platform != "linux", reason="Actual /proc only on Linux")
def test_linux_monitor_flushes_and_stops_on_signal(tmp_path):
    script = Path(monitor.__file__)
    output = tmp_path / "memory.jsonl"
    child = subprocess.Popen([sys.executable, "-B", str(script), "--job-id", "123",
                              "--root-pid", str(__import__("os").getpid()),
                              "--output", str(output), "--interval", "0.05"])
    try:
        for _ in range(100):
            if output.exists() and output.stat().st_size:
                break
            time.sleep(.02)
        child.send_signal(signal.SIGTERM)
        assert child.wait(timeout=3) == 0
        sample = json.loads(output.read_text().splitlines()[0])
        assert sample["root_alive"]
        assert child.pid in {p["pid"] for p in sample["processes"]}
    finally:
        if child.poll() is None:
            child.kill()
            child.wait()
