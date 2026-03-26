
import pytest
from string_utils.validation import __ISBNChecker

def test_none_input():
    with pytest.raises(TypeError):
        checker = __ISBNChecker(None, True)
        checker.is_isbn_10()
