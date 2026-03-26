
import pytest
from string_utils.validation import CREDIT_CARDS

@pytest.mark.parametrize("input_string, expected", [
    ('5432790782910562', True),  # Valid MasterCard number
    ('4532790782910562', False), # Invalid VISA number
    (None, False),               # None input should return False
    ('', False),                 # Empty string should return False
])
def test_valid_mastercard(input_string, expected):
    if input_string is None or input_string == '':
        assert not is_credit_card(input_string)
    else:
        assert is_credit_card(input_string, card_type='MASTERCARD') == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_credit_card_1_test_valid_mastercard
python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1_test_valid_mastercard.py:13:19: E0602: Undefined variable 'is_credit_card' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1_test_valid_mastercard.py:15:15: E0602: Undefined variable 'is_credit_card' (undefined-variable)


"""