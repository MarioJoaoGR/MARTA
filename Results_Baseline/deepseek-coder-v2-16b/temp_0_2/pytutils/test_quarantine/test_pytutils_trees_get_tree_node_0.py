
import pytest
from pytutils.trees import get_tree_node

# Test cases for fetching a specific node
def test_fetching_specific_node():
    tree = {'a': {'b': {'c': 1}}}
    result = get_tree_node(tree, 'a:b:c')
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

pytutils/Test4DT_tests/test_pytutils_trees_get_tree_node_0.py F          [100%]

=================================== FAILURES ===================================
_________________________ test_fetching_specific_node __________________________

    def test_fetching_specific_node():
        tree = {'a': {'b': {'c': 1}}}
>       result = get_tree_node(tree, 'a:b:c')

pytutils/Test4DT_tests/test_pytutils_trees_get_tree_node_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = {'a': {'b': {'c': 1}}}, key = ['a', 'b', 'c']
default = <object object at 0x7f032540efd0>, parent = False

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
FAILED pytutils/Test4DT_tests/test_pytutils_trees_get_tree_node_0.py::test_fetching_specific_node
============================== 1 failed in 0.06s ===============================
"""