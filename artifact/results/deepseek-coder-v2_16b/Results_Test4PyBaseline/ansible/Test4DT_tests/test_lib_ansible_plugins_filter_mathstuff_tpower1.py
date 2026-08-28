
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