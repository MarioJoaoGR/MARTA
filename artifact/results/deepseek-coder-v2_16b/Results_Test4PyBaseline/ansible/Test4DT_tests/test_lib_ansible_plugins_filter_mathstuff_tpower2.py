
import pytest
import math
from ansible.errors import AnsibleFilterTypeError

# Import the function from the specified module
def power(x, y):
    try:
        return math.pow(x, y)
    except TypeError as e:
        raise AnsibleFilterTypeError('pow() can only be used on numbers: %s' % str(e))

# Test cases for the power function
def test_power_basic():
    assert power(2, 3) == pytest.approx(8.0)
    assert power(10, -1) == pytest.approx(0.1)

def test_power_float():
    assert power(2.5, 2) == pytest.approx(6.25)