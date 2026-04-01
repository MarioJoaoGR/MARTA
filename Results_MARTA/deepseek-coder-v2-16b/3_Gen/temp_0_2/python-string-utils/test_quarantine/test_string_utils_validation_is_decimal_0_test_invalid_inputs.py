
import pytest
from string_utils.validation import is_decimal, is_number
from string_utils.errors import InvalidInputError

@pytest.mark.parametrize("test_input", [None, "", "1 2 3", "abc", "1e5"])
def test_invalid_inputs(test_input):
    with pytest.raises(InvalidInputError):
        assert not is_decimal(test_input), f"Expected False for input: {test_input}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_invalid_inputs.py . [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_inputs[] _____________________________

test_input = ''

    @pytest.mark.parametrize("test_input", [None, "", "1 2 3", "abc", "1e5"])
    def test_invalid_inputs(test_input):
>       with pytest.raises(InvalidInputError):
E       Failed: DID NOT RAISE <class 'string_utils.errors.InvalidInputError'>

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_invalid_inputs.py:8: Failed
__________________________ test_invalid_inputs[1 2 3] __________________________

test_input = '1 2 3'

    @pytest.mark.parametrize("test_input", [None, "", "1 2 3", "abc", "1e5"])
    def test_invalid_inputs(test_input):
>       with pytest.raises(InvalidInputError):
E       Failed: DID NOT RAISE <class 'string_utils.errors.InvalidInputError'>

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_invalid_inputs.py:8: Failed
___________________________ test_invalid_inputs[abc] ___________________________

test_input = 'abc'

    @pytest.mark.parametrize("test_input", [None, "", "1 2 3", "abc", "1e5"])
    def test_invalid_inputs(test_input):
>       with pytest.raises(InvalidInputError):
E       Failed: DID NOT RAISE <class 'string_utils.errors.InvalidInputError'>

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_invalid_inputs.py:8: Failed
___________________________ test_invalid_inputs[1e5] ___________________________

test_input = '1e5'

    @pytest.mark.parametrize("test_input", [None, "", "1 2 3", "abc", "1e5"])
    def test_invalid_inputs(test_input):
>       with pytest.raises(InvalidInputError):
E       Failed: DID NOT RAISE <class 'string_utils.errors.InvalidInputError'>

python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_invalid_inputs.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_invalid_inputs.py::test_invalid_inputs[]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_invalid_inputs.py::test_invalid_inputs[1 2 3]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_invalid_inputs.py::test_invalid_inputs[abc]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_decimal_0_test_invalid_inputs.py::test_invalid_inputs[1e5]
========================= 4 failed, 1 passed in 0.04s ==========================
"""