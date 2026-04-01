
import pytest
from unittest.mock import patch
from string_utils.validation import credit_card_validator as cv

def test_empty_string():
    with patch('string_utils.validation.credit_card_validator') as mock_cv:
        mock_cv.is_full_string.return_value = False
        assert not is_credit_card("")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_credit_card_1_test_empty_string
python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1_test_empty_string.py:4:0: E0611: No name 'credit_card_validator' in module 'string_utils.validation' (no-name-in-module)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1_test_empty_string.py:9:19: E0602: Undefined variable 'is_credit_card' (undefined-variable)


"""