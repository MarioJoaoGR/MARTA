
import pytest
from unittest.mock import patch
from __RomanNumbers import __RomanNumbers

def test_valid_case():
    with patch('__RomanNumbers.is_full_string', return_value=True):
        assert __RomanNumbers.decode('XIV') == 14
        assert __RomanNumbers.decode('IX') == 9
        assert __RomanNumbers.decode('MCMXCIV') == 1994

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___RomanNumbers_decode_0_test_valid_case
python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_valid_case.py:4:0: E0401: Unable to import '__RomanNumbers' (import-error)


"""