 Sure, here's the pytest function for testing invalid input type and expecting `InvalidInputError`:

```python
import pytest
from string_utils.manipulation import InvalidInputError
from string_utils.formatter import __StringFormatter

def test_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(12345)
    assert str(exc_info.value) == "Expected 'str', received 'int'"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_duplicates_1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_1_test_invalid_input.py:1:1: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_string_utils_manipulation___StringFormatter___remove_duplicates_1_test_invalid_input, line 1)' (syntax-error)

"""