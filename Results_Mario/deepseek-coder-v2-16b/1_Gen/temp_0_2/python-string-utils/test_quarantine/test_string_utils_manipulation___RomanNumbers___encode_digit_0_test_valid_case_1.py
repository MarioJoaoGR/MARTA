
from unittest.mock import patch
from string_utils.manipulation import __RomanNumbers

def test_valid_case_1():
    with patch.object(__RomanNumbers, '__encode_digit', return_value='III'):
        roman = __RomanNumbers()
        assert roman._RomanNumbers__encode_digit(0, 3) == 'III'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1
python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py:8:15: E1101: Instance of '__RomanNumbers' has no '_RomanNumbers__encode_digit' member (no-member)


"""