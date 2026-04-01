 Here's the pytest function to test invalid input for the `FileSkipComment` exception:

```python
import pytest
from isort.exceptions import FileSkipComment

def test_invalid_input():
    with pytest.raises(FileSkipComment) as excinfo:
        try:
            raise FileSkipComment(123)  # Invalid input type (int instead of str)
        except FileSkipComment as e:
            print(f'The file was skipped because of a comment: {e}')
    assert str(excinfo.value) == "123 contains a file skip comment and was skipped."
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_exceptions_FileSkipComment___init___2_test_invalid_input
isort/Test4DT_tests/test_isort_exceptions_FileSkipComment___init___2_test_invalid_input.py:1:1: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_isort_exceptions_FileSkipComment___init___2_test_invalid_input, line 1)' (syntax-error)


"""