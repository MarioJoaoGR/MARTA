
import pytest
from string_utils.validation import is_credit_card, CREDIT_CARDS

@pytest.mark.parametrize("input_string, expected", [
    ('6011 0009 9013 9424', True),
    ('5100 0009 9013 9424', False),  # Invalid MASTERCARD
    ('3782 8224 6310 005', False),   # Invalid AMERICAN_EXPRESS
    ('6011 0009 9013 9424', True),  # Valid DISCOVER
])
def test_valid_credit_card_discover(input_string, expected):
    assert is_credit_card(input_string, 'DISCOVER') == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_discover.py F [ 25%]
..F                                                                      [100%]

=================================== FAILURES ===================================
__________ test_valid_credit_card_discover[6011 0009 9013 9424-True0] __________

input_string = '6011 0009 9013 9424', expected = True

    @pytest.mark.parametrize("input_string, expected", [
        ('6011 0009 9013 9424', True),
        ('5100 0009 9013 9424', False),  # Invalid MASTERCARD
        ('3782 8224 6310 005', False),   # Invalid AMERICAN_EXPRESS
        ('6011 0009 9013 9424', True),  # Valid DISCOVER
    ])
    def test_valid_credit_card_discover(input_string, expected):
>       assert is_credit_card(input_string, 'DISCOVER') == expected
E       AssertionError: assert False == True
E        +  where False = is_credit_card('6011 0009 9013 9424', 'DISCOVER')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_discover.py:12: AssertionError
__________ test_valid_credit_card_discover[6011 0009 9013 9424-True1] __________

input_string = '6011 0009 9013 9424', expected = True

    @pytest.mark.parametrize("input_string, expected", [
        ('6011 0009 9013 9424', True),
        ('5100 0009 9013 9424', False),  # Invalid MASTERCARD
        ('3782 8224 6310 005', False),   # Invalid AMERICAN_EXPRESS
        ('6011 0009 9013 9424', True),  # Valid DISCOVER
    ])
    def test_valid_credit_card_discover(input_string, expected):
>       assert is_credit_card(input_string, 'DISCOVER') == expected
E       AssertionError: assert False == True
E        +  where False = is_credit_card('6011 0009 9013 9424', 'DISCOVER')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_discover.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_discover.py::test_valid_credit_card_discover[6011 0009 9013 9424-True0]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_0_test_valid_credit_card_discover.py::test_valid_credit_card_discover[6011 0009 9013 9424-True1]
========================= 2 failed, 2 passed in 0.03s ==========================
"""