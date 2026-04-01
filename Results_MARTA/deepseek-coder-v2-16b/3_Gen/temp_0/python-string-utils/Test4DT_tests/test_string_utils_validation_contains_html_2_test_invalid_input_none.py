
import pytest
from string_utils.validation import contains_html, InvalidInputError

def test_invalid_input_none():
    with pytest.raises(InvalidInputError):
        contains_html(None)
