 Here's a pytest function that tests the `__StringFormatter` class for invalid input, specifically raising an `InvalidInputError`:

```python
import pytest
from string_utils.manipulation import is_string, InvalidInputError

class __StringFormatter:
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)
        self.input_string = input_string

def test_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(12345)
    assert str(exc_info.value) == "12345"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___ensure_right_space_only_3_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_3_test_invalid_input.py:1:1: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_string_utils_manipulation___StringFormatter___ensure_right_space_only_3_test_invalid_input, line 1)' (syntax-error)


"""