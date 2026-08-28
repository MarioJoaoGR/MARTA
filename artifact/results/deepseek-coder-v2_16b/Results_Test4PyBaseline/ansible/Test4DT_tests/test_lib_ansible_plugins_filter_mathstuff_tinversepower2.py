
import pytest
import math
from ansible.errors import AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import inversepower

# Test cases for the inversepower function
def test_inversepower_square_root():
    result = inversepower(4)
    assert round(result, 10) == pytest.approx(2.0), f"Expected square root of 4 to be exactly 2.0, but got {result}"

def test_inversepower_cube_root():
    result = inversepower(8, base=3)
    assert round(result, 10) == pytest.approx(2.0), f"Expected cube root of 8 with base 3 to be approximately 2.0, but got {result}"

def test_inversepower_fourth_root():
    result = inversepower(16, base=4)
    assert round(result, 10) == pytest.approx(2.0), f"Expected fourth root of 16 with base 4 to be approximately 2.0, but got {result}"

def test_inversepower_invalid_input():
    with pytest.raises(AnsibleFilterTypeError) as e:
        inversepower('a', base=2)