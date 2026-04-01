
import pytest
from string_utils.validation import is_credit_card, CREDIT_CARDS

@pytest.mark.parametrize("card_number, expected", [('6011 0000 0000 0008', True), ('4111 1111 1111 1111', False)])
def test_valid_input_discover(card_number, expected):
    assert is_credit_card(card_number) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_discover.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_____________ test_valid_input_discover[6011 0000 0000 0008-True] ______________

card_number = '6011 0000 0000 0008', expected = True

    @pytest.mark.parametrize("card_number, expected", [('6011 0000 0000 0008', True), ('4111 1111 1111 1111', False)])
    def test_valid_input_discover(card_number, expected):
>       assert is_credit_card(card_number) == expected
E       AssertionError: assert False == True
E        +  where False = is_credit_card('6011 0000 0000 0008')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_discover.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_discover.py::test_valid_input_discover[6011 0000 0000 0008-True]
========================= 1 failed, 1 passed in 0.03s ==========================
"""