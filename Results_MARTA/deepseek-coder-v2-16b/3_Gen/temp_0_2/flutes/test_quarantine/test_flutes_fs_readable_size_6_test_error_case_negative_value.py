
import pytest
from flutes.fs import readable_size

@pytest.mark.parametrize("size", [-1, -1024, -1024**2])
def test_error_case_negative_value(size):
    with pytest.raises(ValueError):
        readable_size(size)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_error_case_negative_value.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_error_case_negative_value[-1] ______________________

size = -1

    @pytest.mark.parametrize("size", [-1, -1024, -1024**2])
    def test_error_case_negative_value(size):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_error_case_negative_value.py:7: Failed
____________________ test_error_case_negative_value[-1024] _____________________

size = -1024

    @pytest.mark.parametrize("size", [-1, -1024, -1024**2])
    def test_error_case_negative_value(size):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_error_case_negative_value.py:7: Failed
___________________ test_error_case_negative_value[-1048576] ___________________

size = -1048576

    @pytest.mark.parametrize("size", [-1, -1024, -1024**2])
    def test_error_case_negative_value(size):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_error_case_negative_value.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_error_case_negative_value.py::test_error_case_negative_value[-1]
FAILED flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_error_case_negative_value.py::test_error_case_negative_value[-1024]
FAILED flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_error_case_negative_value.py::test_error_case_negative_value[-1048576]
============================== 3 failed in 0.10s ===============================
"""