
from unittest.mock import patch
import pytest
from string_utils.manipulation import slugify, is_string
from string_utils.errors import InvalidInputError

def test_invalid_inputs():
    with patch('string_utils.manipulation.is_string', return_value=False):
        with pytest.raises(InvalidInputError) as exc_info:
            slugify("Test Input")
        assert str(exc_info.value) == "InvalidInputError"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with patch('string_utils.manipulation.is_string', return_value=False):
            with pytest.raises(InvalidInputError) as exc_info:
                slugify("Test Input")
>           assert str(exc_info.value) == "InvalidInputError"
E           assert 'Expected "st...eceived "str"' == 'InvalidInputError'
E             
E             - InvalidInputError
E             + Expected "str", received "str"

python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_2_test_invalid_inputs.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""