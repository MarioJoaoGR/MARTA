
import pytest
import math
from ansible.plugins.filter.mathstuff import inversepower, AnsibleFilterTypeError

# Test valid inputs
def test_valid_inputs():
    assert inversepower(16, 2) == 4.0
    assert inversepower(8, 3) == pytest.approx(2.0, rel=1e-9)

# Test edge cases including None and empty values
def test_edge_cases():
    with pytest.raises(AnsibleFilterTypeError):
        inversepower(None, 3)
    with pytest.raises(AnsibleFilterTypeError):
        inversepower('', 3)

# Test invalid inputs to check error handling
def test_invalid_inputs():
    with pytest.raises(AnsibleFilterTypeError):
        inversepower('a', 2)
