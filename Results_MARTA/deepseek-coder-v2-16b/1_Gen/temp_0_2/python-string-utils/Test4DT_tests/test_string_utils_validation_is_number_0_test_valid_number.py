
import re
import pytest
from string_utils.validation import InvalidInputError, is_number

# Define the regex pattern for matching numbers
NUMBER_RE = re.compile(r"""^[-+]? # Optional sign at the start
                           (?:0|[1-9]\d*)  # Number without leading zeros
                           (?:\.\d+)?     # Optional decimal part
                           (?:[eE][-+]?\d+)? # Optional exponential part
                           $""", re.X)

def test_valid_number():
    assert is_number('42')
    assert is_number('19.99')
    assert is_number('-9.12')
    assert is_number('1e3')
    assert not is_number('1 2 3')
    assert not is_number('abc')
    assert not is_number('+')
    assert not is_number('-')
    assert not is_number('.')
    assert not is_number('e5')
    assert not is_number('1e')

# Add more tests if necessary to cover all edge cases and invalid inputs.
