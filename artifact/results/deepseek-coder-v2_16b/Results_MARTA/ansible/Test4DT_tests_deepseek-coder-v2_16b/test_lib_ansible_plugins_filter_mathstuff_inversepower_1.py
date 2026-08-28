
import pytest
import math
from ansible.plugins.filter.mathstuff import inversepower, AnsibleFilterTypeError

# Test valid inputs
def test_valid_inputs():
    assert inversepower(4) == 2.0
    assert inversepower(8, 3) == pytest.approx(2.0, rel=1e-9)

# Test edge cases
def test_edge_cases():
    with pytest.raises(AnsibleFilterTypeError):
        inversepower('a')
    with pytest.raises(AnsibleFilterTypeError):
        inversepower(None)
    with pytest.raises(AnsibleFilterTypeError):
        inversepower([], 2)

# Test invalid inputs
def test_invalid_inputs():
    with pytest.raises(AnsibleFilterTypeError):
        inversepower('a', 'b')
    with pytest.raises(AnsibleFilterTypeError):
        inversepower('a', None)
    with pytest.raises(AnsibleFilterTypeError):
        inversepower('a', [])
