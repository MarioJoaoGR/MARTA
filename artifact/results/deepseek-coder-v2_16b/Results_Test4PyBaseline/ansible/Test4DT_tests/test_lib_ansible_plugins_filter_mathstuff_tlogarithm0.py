
import pytest
import math
from ansible.plugins.filter.mathstuff import logarithm, AnsibleFilterTypeError

# Test cases for logarithm function with default base (natural logarithm)
def test_logarithm_default_base():
    assert math.isclose(logarithm(100), 4.605170185988092, rel_tol=1e-09)

# Test cases for logarithm function with specified base (common logarithm)
def test_logarithm_specified_base():
    assert math.isclose(logarithm(100, base=10), 2.0, rel_tol=1e-09)

# Test case to check the exception for invalid input
def test_logarithm_invalid_input():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        logarithm(-5)
    assert str(excinfo.value) == 'log() can only be used on numbers: must be real number, not complex'
