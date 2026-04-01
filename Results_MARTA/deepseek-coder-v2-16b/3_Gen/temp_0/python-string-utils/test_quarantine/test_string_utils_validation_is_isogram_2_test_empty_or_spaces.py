
from string_utils.validation import is_isogram

def test_empty_or_spaces():
    assert not is_isogram('')  # An empty string should return False
    assert not is_isogram(' ')  # A string with only spaces should return False
    assert not is_isogram('   ')  # Multiple spaces should also return False
    assert not is_isogram('-')  # A string with a hyphen should return False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_2_test_empty_or_spaces.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_empty_or_spaces _____________________________

    def test_empty_or_spaces():
        assert not is_isogram('')  # An empty string should return False
        assert not is_isogram(' ')  # A string with only spaces should return False
        assert not is_isogram('   ')  # Multiple spaces should also return False
>       assert not is_isogram('-')  # A string with a hyphen should return False
E       AssertionError: assert not True
E        +  where True = is_isogram('-')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_2_test_empty_or_spaces.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_2_test_empty_or_spaces.py::test_empty_or_spaces
============================== 1 failed in 0.02s ===============================
"""