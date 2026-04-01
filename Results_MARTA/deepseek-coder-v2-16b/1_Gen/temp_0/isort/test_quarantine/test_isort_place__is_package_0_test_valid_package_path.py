
from pathlib import Path
from unittest.mock import patch
from isort.place import exists_case_sensitive
import pytest

def _is_package(path: Path) -> bool:
    """Determines if a given path is a package by checking if the path exists and is a directory on Windows, considering case sensitivity, or if it exists on any operating system.

    Parameters:
        path (Path): The file system path to check for existence and whether it's a directory. It should be an instance of Path representing the full path to the file or directory you want to verify.

    Returns:
        bool: True if the path exists as a directory on Windows, considering case sensitivity, or if it exists on any operating system; False otherwise.

    Examples:
        >>> _is_package(Path("C:\\path\\to\\package"))
        True
        >>> _is_package(Path("C:\\path\\to\\Package"))
        False
        >>> _is_package(Path("/usr/local/lib/python/package"))
        True
    """
    return exists_case_sensitive(str(path)) and path.is_dir()

@pytest.mark.parametrize("test_input, expected", [
    (Path("C:\\path\\to\\package"), True),
    (Path("C:\\path\\to\\Package"), False),
    (Path("/usr/local/lib/python/package"), True),
])
def test_is_package(test_input, expected):
    with patch('isort.place.exists_case_sensitive', return_value=True):
        assert _is_package(test_input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_place__is_package_0_test_valid_package_path.py F [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_is_package[test_input0-True] _______________________

test_input = PosixPath('C:\\path\\to\\package'), expected = True

    @pytest.mark.parametrize("test_input, expected", [
        (Path("C:\\path\\to\\package"), True),
        (Path("C:\\path\\to\\Package"), False),
        (Path("/usr/local/lib/python/package"), True),
    ])
    def test_is_package(test_input, expected):
        with patch('isort.place.exists_case_sensitive', return_value=True):
>           assert _is_package(test_input) == expected
E           AssertionError: assert False == True
E            +  where False = _is_package(PosixPath('C:\\path\\to\\package'))

isort/Test4DT_tests/test_isort_place__is_package_0_test_valid_package_path.py:33: AssertionError
______________________ test_is_package[test_input2-True] _______________________

test_input = PosixPath('/usr/local/lib/python/package'), expected = True

    @pytest.mark.parametrize("test_input, expected", [
        (Path("C:\\path\\to\\package"), True),
        (Path("C:\\path\\to\\Package"), False),
        (Path("/usr/local/lib/python/package"), True),
    ])
    def test_is_package(test_input, expected):
        with patch('isort.place.exists_case_sensitive', return_value=True):
>           assert _is_package(test_input) == expected
E           AssertionError: assert False == True
E            +  where False = _is_package(PosixPath('/usr/local/lib/python/package'))

isort/Test4DT_tests/test_isort_place__is_package_0_test_valid_package_path.py:33: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__is_package_0_test_valid_package_path.py::test_is_package[test_input0-True]
FAILED isort/Test4DT_tests/test_isort_place__is_package_0_test_valid_package_path.py::test_is_package[test_input2-True]
========================= 2 failed, 1 passed in 0.10s ==========================
"""