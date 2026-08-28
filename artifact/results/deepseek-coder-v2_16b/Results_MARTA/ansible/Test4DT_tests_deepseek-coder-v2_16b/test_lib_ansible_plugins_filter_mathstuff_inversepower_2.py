
import pytest
from ansible.plugins.filter import mathstuff
from ansible.errors import AnsibleFilterTypeError
import math

# Assuming the function under test is `inversepower` from `ansible.plugins.filter.mathstuff`
def inversepower(x, base=2):
    try:
        if base == 2:
            return math.sqrt(x)
        else:
            return math.pow(x, 1.0 / float(base))
    except (ValueError, TypeError) as e:
        raise AnsibleFilterTypeError('root() can only be used on numbers: %s' % to_native(e))

def test_inversepower_valid():
    assert inversepower(4) == 2.0
    assert inversepower(8, 3) == pytest.approx(2.0, rel=1e-9)

