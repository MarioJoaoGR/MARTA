
# Module: string_utils.manipulation
# test_string_utils.manipulation.py
from string_utils.manipulation import __RomanNumbers

def test__index_for_sign():
    roman_numerals = __RomanNumbers()
    
    # Test valid single Roman numeral signs
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0.py F [100%]

=================================== FAILURES ===================================
_____________________________ test__index_for_sign _____________________________

    def test__index_for_sign():
        roman_numerals = __RomanNumbers()
    
        # Test valid single Roman numeral signs
>       assert roman_numerals.__index_for_sign('I') == 0
E       AttributeError: '__RomanNumbers' object has no attribute '__index_for_sign'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0.py:10: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___index_for_sign_0.py::test__index_for_sign
============================== 1 failed in 0.02s ===============================

"""