
import pytest
from pathlib import Path
import os
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
                yield entry.path

@pytest.mark.parametrize("path", [123, None])
def test_invalid_path(path):
    with pytest.raises(TypeError):
        list(scandir(path))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_fs_scandir_1_test_invalid_path.py FF    [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_path[123] ____________________________

path = 123

    @pytest.mark.parametrize("path", [123, None])
    def test_invalid_path(path):
        with pytest.raises(TypeError):
>           list(scandir(path))

flutes/Test4DT_tests/test_flutes_fs_scandir_1_test_invalid_path.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = 123

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
>           with os.scandir(path) as it:
E           OSError: [Errno 9] Bad file descriptor

flutes/Test4DT_tests/test_flutes_fs_scandir_1_test_invalid_path.py:21: OSError
___________________________ test_invalid_path[None] ____________________________

path = None

    @pytest.mark.parametrize("path", [123, None])
    def test_invalid_path(path):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_fs_scandir_1_test_invalid_path.py:27: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_scandir_1_test_invalid_path.py::test_invalid_path[123]
FAILED flutes/Test4DT_tests/test_flutes_fs_scandir_1_test_invalid_path.py::test_invalid_path[None]
============================== 2 failed in 0.06s ===============================

"""