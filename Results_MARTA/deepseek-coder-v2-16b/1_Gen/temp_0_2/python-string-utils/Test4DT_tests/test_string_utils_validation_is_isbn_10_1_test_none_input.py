
import pytest
from string_utils.validation import is_isbn_10

def test_none_input():
    with pytest.raises(TypeError):
        assert is_isbn_10(None)
