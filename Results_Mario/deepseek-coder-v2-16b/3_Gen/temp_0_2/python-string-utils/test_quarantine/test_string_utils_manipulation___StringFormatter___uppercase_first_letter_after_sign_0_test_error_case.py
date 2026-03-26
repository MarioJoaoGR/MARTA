
import pytest
from string_utils.manipulation import InvalidInputError, is_string

class __StringFormatter:
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)
        self.input_string = input_string

def test_error_case():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(12345)
    
    assert isinstance(exc_info.value, InvalidInputError)
    assert exc_info.value.args[0] == 12345

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_0_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        with pytest.raises(InvalidInputError) as exc_info:
            formatter = __StringFormatter(12345)
    
        assert isinstance(exc_info.value, InvalidInputError)
>       assert exc_info.value.args[0] == 12345
E       assert 'Expected "str", received "int"' == 12345

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_0_test_error_case.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_0_test_error_case.py::test_error_case
============================== 1 failed in 0.03s ===============================
"""