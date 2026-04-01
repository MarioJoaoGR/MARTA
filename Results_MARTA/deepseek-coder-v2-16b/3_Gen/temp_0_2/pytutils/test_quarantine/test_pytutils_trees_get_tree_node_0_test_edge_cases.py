
import pytest
from pytutils.trees import get_tree_node, _sentinel

def test_edge_cases():
    mapping = {'a': {'b': {'c': 1}}}
    
    # Test with None key
    with pytest.raises(KeyError):
        get_tree_node(mapping, None)

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

pytutils/Test4DT_tests/test_pytutils_trees_get_tree_node_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        mapping = {'a': {'b': {'c': 1}}}
    
        # Test with None key
        with pytest.raises(KeyError):
>           get_tree_node(mapping, None)

pytutils/Test4DT_tests/test_pytutils_trees_get_tree_node_0_test_edge_cases.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = {'a': {'b': {'c': 1}}}, key = None
default = <object object at 0x7f419e76afd0>, parent = False

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
>       key = key.split(':')
E       AttributeError: 'NoneType' object has no attribute 'split'

pytutils/pytutils/trees.py:20: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_trees_get_tree_node_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.06s ===============================
"""