
import pytest
from collections import MutableMapping
from ansible.errors import AnsibleError
from ansible.utils.vars import dumps, to_native

# Assuming the function is part of a module named 'ansible.utils.vars'
# and that it has been imported correctly as shown in the provided code.

def test__validate_mutable_mappings_basic():
    # Test with two valid mutable mappings (dictionaries)
    dict1 = {'a': 1}
    dict2 = {'b': 2}
    
    try:
        _validate_mutable_mappings(dict1, dict2)
    except AnsibleError as e:
        pytest.fail(f"Unexpected error occurred: {e}")
    
    # Test with one valid mutable mapping and one invalid (string)
    str_val = "not a dictionary"
    try:
        _validate_mutable_mappings({'a': 1}, str_val)
        pytest.fail("Expected AnsibleError but did not get it")
    except AnsibleError as e:
        assert str(e) == "failed to combine variables, expected dicts but got a 'dict' and a 'str': \n{'a': 1}\nnot a dictionary"
    
    # Test with two invalid types (integer and string)
    try:
        _validate_mutable_mappings(42, "string")
        pytest.fail("Expected AnsibleError but did not get it")
    except AnsibleError as e:
        assert str(e) == "failed to combine variables, expected dicts but got a 'int' and a 'str': \n42\nstring"
    
    # Test with two valid mutable mappings (subclass of MutableMapping)
    class MyMutableMapping(dict):
        pass

    dict1 = MyMutableMapping({'a': 1})
    dict2 = MyMutableMapping({'b': 2})
    try:
        _validate_mutable_mappings(dict1, dict2)
    except AnsibleError as e:
        pytest.fail(f"Unexpected error occurred: {e}")
