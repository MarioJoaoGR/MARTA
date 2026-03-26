
import pytest
from string_utils.validation import words_count, InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        assert words_count('')  # This should raise an InvalidInputError because the input is empty
        assert words_count(None)  # This should raise an InvalidInputError because the input is None
        assert words_count(12345)  # This should raise an InvalidInputError because the input is not a string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(InvalidInputError):
>           assert words_count('')  # This should raise an InvalidInputError because the input is empty
E           AssertionError: assert 0
E            +  where 0 = words_count('')

python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_1_test_invalid_input.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""