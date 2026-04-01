
import os
from pathlib import Path
from typing import Iterator
from flutes.fs import scandir

def test_valid_input_string():
    valid_input = Path('/some/directory')
    result = list(scandir(valid_input))
    assert len(result) > 0, "Expected a non-empty directory"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_valid_input_string.py F [100%]

=================================== FAILURES ===================================
___________________________ test_valid_input_string ____________________________

    def test_valid_input_string():
        valid_input = Path('/some/directory')
>       result = list(scandir(valid_input))

flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_valid_input_string.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = PosixPath('/some/directory')

    def scandir(path: PathType) -> Iterator[PathType]:
        r"""Lazily iterate over all files and directories under a directory. The returned path is the absolute path of the
        child file or directory, with the same type as :attr:`path` (:py:class:`pathlib.Path` or :py:class:`str`).
    
        :param path: Path to the directory.
        :return: An iterator over children paths.
        """
        if isinstance(path, Path):
>           with os.scandir(path) as it:
E           FileNotFoundError: [Errno 2] No such file or directory: '/some/directory'

flutes/flutes/fs.py:169: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_valid_input_string.py::test_valid_input_string
============================== 1 failed in 0.09s ===============================
"""