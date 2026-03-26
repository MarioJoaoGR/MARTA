
# Module: pytutils.mappings
import pytest
from collections import UserDict, MutableMapping
from pytutils.mappings import ProxyMutableMapping

# Example 1: Basic Usage with a Dictionary
def test_basic_usage():
    a = {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}
    proxy_mapping = ProxyMutableMapping(a)
    
    assert proxy_mapping['whoa'] == True
    proxy_mapping['nice'] = False
    assert a == {'whoa': True, 'hello': [1, 2, 3], 'why': 'always', 'nice': False}

# Example 2: Using `fancy_repr` and `dictify_repr` Parameters
def test_fancy_and_dictify_repr():
    a = {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}
    
    b = ProxyMutableMapping(a, fancy_repr=True)
    assert str(b) == "<ProxyMutableMapping {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>"
    
    c = ProxyMutableMapping(a, dictify_repr=True)
    assert str(c) == {"whoa": True, "hello": [1, 2, 3], "why": "always"}

# Example 3: Using a Custom Mapping Type (e.g., `UserDict`)
def test_custom_mapping():
    from collections import UserDict
    
    custom_mapping = UserDict({'whoa': True, 'hello': [1, 2, 3], 'why': 'always'})
    proxy_mapping_custom = ProxyMutableMapping(custom_mapping)
    
    assert proxy_mapping_custom['whoa'] == True

# Example 4: Chaining Methods (if applicable)
def test_chaining_methods():
    d = ProxyMutableMapping({'whoa': True, 'hello': [1, 2, 3], 'why': 'always'})
    d['nice'] = False
    d['whoa'] = 'yeee'
    
    assert str(d) == "<ProxyMutableMapping {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False}>"

# Example 5: Using `fancy_repr` and `dictify_repr` with Custom Representation
def test_fancy_and_dictify_with_custom_representation():
    a = {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}
    
    d = ProxyMutableMapping(a, fancy_repr=True, dictify_repr=True)
    assert str(d) == {"whoa": True, "hello": [1, 2, 3], "why": "always"}

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableMapping__set_mapping_0
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping__set_mapping_0.py:4:0: E0611: No name 'MutableMapping' in module 'collections' (no-name-in-module)


"""