
# Module: flutes.fs
import pytest
from flutes.fs import remove_prefix

# Test cases for remove_prefix function
def test_remove_prefix_fully_matching():
    assert remove_prefix("https://github.com/huzecong/flutes", "https://") == 'github.com/huzecong/flutes'

def test_remove_prefix_non_fully_matching():
    assert remove_prefix("preface", "prefix", fully_match=False) == 'face'

def test_remove_prefix_empty_string():
    assert remove_prefix("", "https://") == ''

def test_remove_prefix_exact_match():
    assert remove_prefix("https://github.com/huzecong/flutes", "https://") == 'github.com/huzecong/flutes'

def test_remove_prefix_no_match():
    assert remove_prefix("https://github.com/huzecong/flutes", "http") == 'https://github.com/huzecong/flutes'

def test_remove_prefix_custom_prefix_length():
    assert remove_prefix("https://github.com/huzecong/flutes", "https://", fully_match=False) == 'github.com/huzecong/flutes'

# Additional edge cases to consider:
def test_remove_prefix_fully_matching_with_default():
    assert remove_prefix("https://github.com/huzecong/flutes") == 'github.com/huzecong/flutes'  # Default fully_match=True, but should behave as if fully_match=False for this case

def test_remove_prefix_non_fully_matching_with_default():
    assert remove_prefix("preface", "prefix") == 'face'  # Default fully_match=True, but should behave as if fully_match=False for this case

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_remove_prefix_0
flutes/Test4DT_tests/test_flutes_fs_remove_prefix_0.py:27:11: E1120: No value for argument 'prefix' in function call (no-value-for-parameter)


"""