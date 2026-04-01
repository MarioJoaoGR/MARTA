
import pytest
from string_utils.validation import is_isbn_10

def test_error_handling():
    # Test case 1: Non-string input should raise a TypeError
    with pytest.raises(TypeError):
        is_isbn_10(12345)
    
    # Test case 2: Incorrect type for normalize parameter should raise a TypeError
    with pytest.raises(TypeError):
        is_isbn_10('12345', normalize=123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_2_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        # Test case 1: Non-string input should raise a TypeError
        with pytest.raises(TypeError):
            is_isbn_10(12345)
    
        # Test case 2: Incorrect type for normalize parameter should raise a TypeError
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_2_test_error_handling.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_2_test_error_handling.py::test_error_handling
============================== 1 failed in 0.03s ===============================

"""