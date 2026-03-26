 Here's the pytest function to test handling non-string input and expecting `InvalidInputError`:

```python
import pytest
from string_utils.manipulation import is_string, InvalidInputError
from __StringFormatter import __StringFormatter

def test_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(12345)  # This should raise InvalidInputError
    
    assert str(exc_info.value) == "Expected 'str', received 'int'"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_1_test_invalid_input.py:1:1: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_1_test_invalid_input, line 1)' (syntax-error)

"""