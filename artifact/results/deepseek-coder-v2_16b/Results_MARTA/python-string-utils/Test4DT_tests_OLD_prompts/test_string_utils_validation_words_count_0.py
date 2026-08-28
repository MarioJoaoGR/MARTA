
import pytest
from unittest.mock import patch
from string_utils.validation import words_count, InvalidInputError
import re

# Test valid input with multiple words and punctuation
def test_valid_input():
    with patch('string_utils.validation.WORDS_COUNT_RE', new=re.compile(r'\b\w+\b')):
        assert words_count('hello world') == 2
        assert words_count('one,two,three.stop') == 4

# Test invalid input with no letters or numbers

# Test empty input
def test_empty_input():
    with patch('string_utils.validation.WORDS_COUNT_RE', new=re.compile(r'\b\w+\b')):
        assert words_count('') == 0