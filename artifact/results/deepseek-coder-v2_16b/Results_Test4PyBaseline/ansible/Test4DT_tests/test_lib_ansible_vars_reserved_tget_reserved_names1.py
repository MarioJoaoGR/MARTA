
# Module: ansible.vars.reserved
# test_get_reserved_names.py
from ansible.vars.reserved import get_reserved_names

def test_default_usage():
    reserved_names = get_reserved_names()
    assert isinstance(reserved_names, set), "Expected a set of names"
    # Add more specific assertions based on the expected output for default usage