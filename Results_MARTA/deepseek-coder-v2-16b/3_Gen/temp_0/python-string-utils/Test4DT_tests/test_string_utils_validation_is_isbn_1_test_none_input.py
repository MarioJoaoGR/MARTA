
import pytest
from string_utils.validation import is_isbn, __ISBNChecker
from string_utils.errors import InvalidInputError

def test_none_input():
    with pytest.raises(InvalidInputError):
        assert not is_isbn(None)  # Test for None input
