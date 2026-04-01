
import pytest
from string_utils.manipulation import __RomanNumbers

def test_valid_input():
    mockClass = __RomanNumbers()
    
    # Test valid Roman numeral signs
    assert mockClass.__index_for_sign('I') == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        mockClass = __RomanNumbers()
    
        # Test valid Roman numeral signs
>       assert mockClass.__index_for_sign('I') == 0
E       AttributeError: '__RomanNumbers' object has no attribute '__index_for_sign'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_valid_input.py:9: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""