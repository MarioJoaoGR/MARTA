
import pytest
from ansible.errors import AnsibleFilterTypeError
import math

def power(x, y):
    try:
        return math.pow(x, y)
    except TypeError as e:
        raise AnsibleFilterTypeError('pow() can only be used on numbers: %s' % str(e))

# Test cases for edge cases and invalid input types
def test_edge_cases():
    with pytest.raises(AnsibleFilterTypeError):
        power(None, None)

def test_invalid_input_types():
    with pytest.raises(AnsibleFilterTypeError):
        power('a', 'b')
