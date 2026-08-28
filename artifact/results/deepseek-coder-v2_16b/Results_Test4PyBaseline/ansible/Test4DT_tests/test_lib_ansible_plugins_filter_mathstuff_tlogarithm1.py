
import pytest
import math
from ansible.plugins.filter.mathstuff import logarithm, AnsibleFilterTypeError

# Test cases for logarithm function with default base (natural logarithm)
def test_logarithm_default_base():
    assert math.isclose(logarithm(100), 4.605170185988092, rel_tol=1e-09)
    # Additional test for natural logarithm with a different number