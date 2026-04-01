
import pytest
from pytutils.trees import get_tree_node, _sentinel

def test_valid_inputs():
    mapping = {'a': {'b': {'c': 1}}}
    
    # Test fetching a direct value
    assert get_tree_node(mapping, 'a:b:c') == 1

    # Test fetching with default value when key does not exist
    assert get_tree_node(mapping, 'a:b:d', default=None) is None

    # Test fetching parent node
    assert get_tree_node(mapping, 'a:b', parent=True) == {'c': 1}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_trees_get_tree_node_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        mapping = {'a': {'b': {'c': 1}}}
    
        # Test fetching a direct value
>       assert get_tree_node(mapping, 'a:b:c') == 1

pytutils/Test4DT_tests/test_pytutils_trees_get_tree_node_0_test_valid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = {'a': {'b': {'c': 1}}}, key = ['a', 'b', 'c']
default = <object object at 0x7fd51502ba40>, parent = False

    def get_tree_node(mapping, key, default=_sentinel, parent=False):
        """
        Fetch arbitrary node from a tree-like mapping structure with traversal help:
        Dimension can be specified via ':'
    
        Arguments:
            mapping collections.Mapping: Mapping to fetch from
            key str|unicode: Key to lookup, allowing for : notation
            default object: Default value. If set to `:module:_sentinel`, raise KeyError if not found.
            parent bool: If True, return parent node. Defaults to False.
    
        Returns:
            object: Value at specified key
        """
        key = key.split(':')
        if parent:
            key = key[:-1]
    
        # TODO Unlist my shit. Stop calling me please.
    
        node = mapping
>       for node in key.split(':'):
E       AttributeError: 'list' object has no attribute 'split'

pytutils/pytutils/trees.py:27: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_trees_get_tree_node_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.05s ===============================
"""