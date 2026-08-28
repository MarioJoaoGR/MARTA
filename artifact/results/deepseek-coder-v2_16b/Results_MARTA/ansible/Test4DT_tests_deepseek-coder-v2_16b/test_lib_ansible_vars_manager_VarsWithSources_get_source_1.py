
import pytest
from ansible.vars.manager import VarsWithSources

def test_invalid_input():
    vs = VarsWithSources()
    with pytest.raises(KeyError):
        vs['non_existent_key']  # Accessing a non-existent key should raise a KeyError
