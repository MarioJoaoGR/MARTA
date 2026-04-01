
import re
from string_utils.validation import is_number

# Define a mock for NUMBER_RE if it's used in the actual implementation
NUMBER_RE = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')

def test_valid_numbers():
    # Test cases for valid numbers
    assert is_number('42')  # True, integer
    assert is_number('19.99')  # True, float
    assert is_number('-9.12')  # True, negative float
    assert is_number('1e3')  # True, scientific notation
    assert not is_number('1 2 3')  # False, invalid format
