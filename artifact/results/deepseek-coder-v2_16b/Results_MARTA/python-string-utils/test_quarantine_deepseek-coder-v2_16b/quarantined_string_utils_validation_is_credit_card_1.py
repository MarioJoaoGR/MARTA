
import pytest
from string_utils.validation import is_credit_card



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_credit_card_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_visa_card _____________________________

    def test_valid_visa_card():
        input_string = '4111 1111 1111 1111'
>       assert is_credit_card(input_string) == True, f"Expected True for a valid VISA card number: {input_string}"
E       AssertionError: Expected True for a valid VISA card number: 4111 1111 1111 1111
E       assert False == True
E        +  where False = is_credit_card('4111 1111 1111 1111')

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_credit_card_1.py:7: AssertionError
________________________ test_valid_multiple_card_types ________________________

    def test_valid_multiple_card_types():
        input_string = '3782 822463 10005'
>       assert is_credit_card(input_string) == True, f"Expected True for a valid card number with no specific type: {input_string}"
E       AssertionError: Expected True for a valid card number with no specific type: 3782 822463 10005
E       assert False == True
E        +  where False = is_credit_card('3782 822463 10005')

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_credit_card_1.py:11: AssertionError
____________________________ test_invalid_card_type ____________________________

    def test_invalid_card_type():
        input_string = '5555 5555 5555 4444'
        with pytest.raises(KeyError) as excinfo:
            is_credit_card(input_string, card_type='INVALID_TYPE')
>       assert str(excinfo.value) == 'Invalid card type "INVALID_TYPE". Valid types are: visa, mastercard, american_express, diners_club, discover, jcb', f"Expected KeyError for invalid card type: {input_string}"
E       AssertionError: Expected KeyError for invalid card type: 5555 5555 5555 4444
E       assert "'Invalid car...ISCOVER, JCB'" == 'Invalid card...discover, jcb'
E         
E         - Invalid card type "INVALID_TYPE". Valid types are: visa, mastercard, american_express, diners_club, discover, jcb
E         + 'Invalid card type "INVALID_TYPE". Valid types are: VISA, MASTERCARD, AMERICAN_EXPRESS, DINERS_CLUB, DISCOVER, JCB'

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_credit_card_1.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_credit_card_1.py::test_valid_visa_card
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_credit_card_1.py::test_valid_multiple_card_types
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation_is_credit_card_1.py::test_invalid_card_type
============================== 3 failed in 0.07s ===============================
"""