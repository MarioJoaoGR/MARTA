
import pytest
from ansible.plugins.filter import mathstuff
from ansible.errors import AnsibleFilterTypeError
import math

# Assuming the function `power` is defined in the `mathstuff` module as per the provided documentation

def test_valid_case():
    assert mathstuff.power(2, 3) == 8.0

def test_edge_case():
    with pytest.raises(AnsibleFilterTypeError):
        mathstuff.power(None, None)

def test_error_case():
    with pytest.raises(AnsibleFilterTypeError):
        mathstuff.power('a', 'b')
