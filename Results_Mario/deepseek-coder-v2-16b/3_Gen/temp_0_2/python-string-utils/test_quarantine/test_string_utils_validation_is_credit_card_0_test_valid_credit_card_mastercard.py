
import pytest
from string_utils.validation import is_credit_card, CREDIT_CARDS

@pytest.mark.parametrize("input_string, expected", [
    ('5555 5555 5555 4444', True),
    ('5105 1051 0510 5100', True),
    ('3782 8224 6310 005', False),  # American Express
    ('6011 1111 1111 1117', False),  # Discover
    ('3530 1113 3330 0000', True),  # JCB
    ('4111 1111 1111 1111', False),  # Visa
])
def test_valid_credit_card_mastercard(input_string, expected):
    assert is_credit_card(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_mastercard.py F [ 16%]
F..F.                                                                    [100%]

=================================== FAILURES ===================================
_________ test_valid_credit_card_mastercard[5555 5555 5555 4444-True] __________

input_string = '5555 5555 5555 4444', expected = True

    @pytest.mark.parametrize("input_string, expected", [
        ('5555 5555 5555 4444', True),
        ('5105 1051 0510 5100', True),
        ('3782 8224 6310 005', False),  # American Express
        ('6011 1111 1111 1117', False),  # Discover
        ('3530 1113 3330 0000', True),  # JCB
        ('4111 1111 1111 1111', False),  # Visa
    ])
    def test_valid_credit_card_mastercard(input_string, expected):
>       assert is_credit_card(input_string) == expected
E       AssertionError: assert False == True
E        +  where False = is_credit_card('5555 5555 5555 4444')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_mastercard.py:14: AssertionError
_________ test_valid_credit_card_mastercard[5105 1051 0510 5100-True] __________

input_string = '5105 1051 0510 5100', expected = True

    @pytest.mark.parametrize("input_string, expected", [
        ('5555 5555 5555 4444', True),
        ('5105 1051 0510 5100', True),
        ('3782 8224 6310 005', False),  # American Express
        ('6011 1111 1111 1117', False),  # Discover
        ('3530 1113 3330 0000', True),  # JCB
        ('4111 1111 1111 1111', False),  # Visa
    ])
    def test_valid_credit_card_mastercard(input_string, expected):
>       assert is_credit_card(input_string) == expected
E       AssertionError: assert False == True
E        +  where False = is_credit_card('5105 1051 0510 5100')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_mastercard.py:14: AssertionError
_________ test_valid_credit_card_mastercard[3530 1113 3330 0000-True] __________

input_string = '3530 1113 3330 0000', expected = True

    @pytest.mark.parametrize("input_string, expected", [
        ('5555 5555 5555 4444', True),
        ('5105 1051 0510 5100', True),
        ('3782 8224 6310 005', False),  # American Express
        ('6011 1111 1111 1117', False),  # Discover
        ('3530 1113 3330 0000', True),  # JCB
        ('4111 1111 1111 1111', False),  # Visa
    ])
    def test_valid_credit_card_mastercard(input_string, expected):
>       assert is_credit_card(input_string) == expected
E       AssertionError: assert False == True
E        +  where False = is_credit_card('3530 1113 3330 0000')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_mastercard.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_mastercard.py::test_valid_credit_card_mastercard[5555 5555 5555 4444-True]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_mastercard.py::test_valid_credit_card_mastercard[5105 1051 0510 5100-True]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_mastercard.py::test_valid_credit_card_mastercard[3530 1113 3330 0000-True]
========================= 3 failed, 3 passed in 0.03s ==========================
"""