
import pytest
from string_utils.validation import words_count, InvalidInputError
import re

# Mocking a regex pattern for demonstration purposes
WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        assert words_count('') == 0
        assert words_count(None) is None
        assert words_count(12345) is None
