
import pytest
from string_utils.validation import is_credit_card

def test_none_input():
    # Test with None input
    input_string = None
    with pytest.raises(TypeError):
        assert is_credit_card(input_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        # Test with None input
        input_string = None
        with pytest.raises(TypeError):
>           assert is_credit_card(input_string)
E           assert False
E            +  where False = is_credit_card(None)

python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1_test_none_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_credit_card_1_test_none_input.py::test_none_input
============================== 1 failed in 0.03s ===============================
"""