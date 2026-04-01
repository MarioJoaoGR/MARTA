
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from isort.place import _src_path_is_module

@pytest.mark.parametrize("src_path, module_name", [
    (Path("non_directory_path"), "modulename")
])
def test_error_case(src_path, module_name):
    with patch('isort.place.exists_case_sensitive', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            _src_path_is_module(src_path, module_name)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_place__src_path_is_module_2_test_error_case.py F [100%]

=================================== FAILURES ===================================
____________________ test_error_case[src_path0-modulename] _____________________

src_path = PosixPath('non_directory_path'), module_name = 'modulename'

    @pytest.mark.parametrize("src_path, module_name", [
        (Path("non_directory_path"), "modulename")
    ])
    def test_error_case(src_path, module_name):
        with patch('isort.place.exists_case_sensitive', side_effect=FileNotFoundError):
>           with pytest.raises(FileNotFoundError):
E           Failed: DID NOT RAISE <class 'FileNotFoundError'>

isort/Test4DT_tests/test_isort_place__src_path_is_module_2_test_error_case.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__src_path_is_module_2_test_error_case.py::test_error_case[src_path0-modulename]
============================== 1 failed in 0.11s ===============================
"""