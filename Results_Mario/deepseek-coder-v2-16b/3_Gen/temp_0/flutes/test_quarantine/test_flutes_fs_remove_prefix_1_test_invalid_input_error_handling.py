
import pytest
from flutes.fs import remove_prefix

def test_invalid_input_error_handling():
    # Test case where prefix does not match and fully_match is True
    with pytest.raises(ValueError):
        remove_prefix("https://github.com/huzecong/flutes", "https://")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_remove_prefix_1_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        # Test case where prefix does not match and fully_match is True
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_fs_remove_prefix_1_test_invalid_input_error_handling.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_prefix_1_test_invalid_input_error_handling.py::test_invalid_input_error_handling
============================== 1 failed in 0.07s ===============================

"""