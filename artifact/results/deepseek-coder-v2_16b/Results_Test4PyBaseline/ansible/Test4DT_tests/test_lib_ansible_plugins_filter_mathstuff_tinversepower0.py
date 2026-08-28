
import pytest
import math
from ansible.errors import AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import inversepower

# Test cases for the inversepower function
def test_inversepower_square_root():
    result = inversepower(8)
    assert round(result, 10) == 2.8284271247, f"Expected square root of 8 to be approximately 2.8284271247, but got {result}"

def test_inversepower_cube_root():
    result = inversepower(27, base=3)
    assert round(result, 10) == 3.0, f"Expected cube root of 27 with base 3 to be approximately 3.0, but got {result}"

def test_inversepower_fourth_root():
    result = inversepower(16, base=4)
    assert round(result, 10) == 2.0, f"Expected fourth root of 16 with base 4 to be approximately 2.0, but got {result}"

def test_inversepower_invalid_input():
    with pytest.raises(AnsibleFilterTypeError) as e:
        inversepower('a', base=2)
    assert str(e.value) == 'root() can only be used on numbers: could not convert string to float: \'a\'', f"Expected error for invalid input, but got {e.value}"

def test_inversepower_invalid_base():
    with pytest.raises(AnsibleFilterTypeError) as e:
        inversepower(8, base='two')
    assert str(e.value) == 'root() can only be used on numbers: could not convert string to float: \'two\'', f"Expected error for invalid base, but got {e.value}"
