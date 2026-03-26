
import pytest
from string_utils.manipulation import snake_case_to_camel, is_snake_case, is_string, InvalidInputError

@pytest.mark.parametrize("test_input", [
    12345,  # int
    None,   # None
    '',     # empty string
])
def test_invalid_inputs(test_input):
    with pytest.raises(InvalidInputError):
        snake_case_to_camel(test_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_3_test_invalid_input.py . [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_inputs[] _____________________________

test_input = ''

    @pytest.mark.parametrize("test_input", [
        12345,  # int
        None,   # None
        '',     # empty string
    ])
    def test_invalid_inputs(test_input):
>       with pytest.raises(InvalidInputError):
E       Failed: DID NOT RAISE <class 'string_utils.errors.InvalidInputError'>

python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_3_test_invalid_input.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_3_test_invalid_input.py::test_invalid_inputs[]
========================= 1 failed, 2 passed in 0.03s ==========================
"""