
import pytest
from pytutils.trees import Tree

def test_namespace_handling():
    # Create a Tree instance with initial data
    tree = Tree({'a': {'b': 1}, 'c': 2})
    
    # Accessing values using keys
    assert tree['a']['b'] == 1
    assert tree['c'] == 2
    
    # Using namespace to create a nested structure
    tree_with_namespace = Tree({'a': {'b': 1}}, namespace='root.')
    assert tree_with_namespace['root.a']['b'] == 1
    
    # Updating the tree with new data
    tree.update({'d': 3})
    assert tree['d'] == 3
    
    # Retrieving values using get method
    assert tree.get('a')['b'] == 1
    assert tree.get('c') == 2
    assert tree.get('root.a')['b'] == 1
    
    # Testing namespace handling in setitem method
    tree_with_namespace = Tree()
    tree_with_namespace['root.a'] = {'b': 1}
    assert tree_with_namespace['root.a']['b'] == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""