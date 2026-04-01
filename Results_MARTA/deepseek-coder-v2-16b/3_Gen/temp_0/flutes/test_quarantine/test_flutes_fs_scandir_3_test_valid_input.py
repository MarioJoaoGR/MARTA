
import os
from pathlib import Path
from typing import Iterator, Union

PathType = Union[str, Path]

def scandir(path: PathType) -> Iterator[PathType]:
    r"""Lazily iterate over all files and directories under a directory. The returned path is the absolute path of the
    child file or directory, with the same type as :attr:`path` (:py:class:`pathlib.Path` or :py:class:`str`).

    :param path: Path to the directory.
    :return: An iterator over children paths.
    """
    if isinstance(path, Path):
        with os.scandir(str(path)) as it:
            for entry in it:
                yield Path(entry.path)
    else:
        with os.scandir(path) as it:
            for entry in it:
                yield entry.path if isinstance(entry, os.DirEntry) else Path(entry.name)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.07s =============================
"""