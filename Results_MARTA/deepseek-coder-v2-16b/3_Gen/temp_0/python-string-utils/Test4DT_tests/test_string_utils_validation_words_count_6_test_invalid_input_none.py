
import pytest
from string_utils.validation import words_count, InvalidInputError

def test_invalid_input_none():
    with pytest.raises(InvalidInputError):
        assert words_count(None) == 0
