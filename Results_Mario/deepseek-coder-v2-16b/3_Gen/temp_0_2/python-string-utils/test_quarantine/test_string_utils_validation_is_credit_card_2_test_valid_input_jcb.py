
import re
from string_utils.validation import is_full_string, CREDIT_CARDS

def test_valid_input_jcb():
    input_string = '3530 1113 3330 0006'
    assert is_full_string(input_string) == True, "Input string should be considered full"
    assert CREDIT_CARDS['JCB'].match(input_string) is not None, "Should validate JCB card number"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_jcb.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_input_jcb _____________________________

    def test_valid_input_jcb():
        input_string = '3530 1113 3330 0006'
        assert is_full_string(input_string) == True, "Input string should be considered full"
>       assert CREDIT_CARDS['JCB'].match(input_string) is not None, "Should validate JCB card number"
E       AssertionError: Should validate JCB card number
E       assert None is not None
E        +  where None = <built-in method match of re.Pattern object at 0x1013d7850>('3530 1113 3330 0006')
E        +    where <built-in method match of re.Pattern object at 0x1013d7850> = re.compile('^(?:2131|1800|35\\d{3})\\d{11}$').match

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_jcb.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_2_test_valid_input_jcb.py::test_valid_input_jcb
============================== 1 failed in 0.03s ===============================
"""