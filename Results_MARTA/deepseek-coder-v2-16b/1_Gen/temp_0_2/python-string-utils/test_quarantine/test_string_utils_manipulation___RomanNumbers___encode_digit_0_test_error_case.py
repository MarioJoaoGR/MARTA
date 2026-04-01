
import pytest
from string_utils.manipulation import __RomanNumbers

def test_error_case():
    mockClass = __RomanNumbers()
    
    with pytest.raises(ValueError):
        mockClass.__encode_digit(0, 10)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        mockClass = __RomanNumbers()
    
        with pytest.raises(ValueError):
>           mockClass.__encode_digit(0, 10)
E           AttributeError: '__RomanNumbers' object has no attribute '__encode_digit'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_error_case.py:9: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_error_case.py::test_error_case
============================== 1 failed in 0.03s ===============================
"""