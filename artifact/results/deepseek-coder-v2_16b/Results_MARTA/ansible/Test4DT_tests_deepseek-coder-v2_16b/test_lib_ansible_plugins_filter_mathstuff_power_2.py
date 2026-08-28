
import pytest
from ansible.plugins.filter import mathstuff
from ansible.errors import AnsibleFilterTypeError
import math

# Assuming the function `power` is defined in the `mathstuff` module
def test_valid_inputs():
    assert mathstuff.power(2, 3) == 8.0
    assert mathstuff.power(4, 0.5) == 2.0

def test_edge_cases():
    with pytest.raises(AnsibleFilterTypeError):
        mathstuff.power(None, None)

def test_invalid_inputs():
    with pytest.raises(AnsibleFilterTypeError):
        mathstuff.power('a', 'b')
