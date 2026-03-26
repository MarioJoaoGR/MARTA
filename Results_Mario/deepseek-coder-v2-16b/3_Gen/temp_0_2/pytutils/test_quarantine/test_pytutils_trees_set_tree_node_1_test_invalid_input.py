
import pytest
from pytutils.trees import set_tree_node, get_tree_node

def test_invalid_input():
    mapping = {}
    
    # Test with invalid key (not a string)
    with pytest.raises(TypeError):
        set_tree_node(mapping, 123, 'value')

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

pytutils/Test4DT_tests/test_pytutils_trees_set_tree_node_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        mapping = {}
    
        # Test with invalid key (not a string)
        with pytest.raises(TypeError):
>           set_tree_node(mapping, 123, 'value')

pytutils/Test4DT_tests/test_pytutils_trees_set_tree_node_1_test_invalid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = {}, key = 123, value = 'value'

    def set_tree_node(mapping, key, value):
        """
        Set arbitrary node on a tree-like mapping structure, allowing for : notation to signify dimension.
    
        Arguments:
            mapping collections.Mapping: Mapping to fetch from
            key str|unicode: Key to set, allowing for : notation
            value str|unicode: Value to set `key` to
            parent bool: If True, return parent node. Defaults to False.
    
        Returns:
            object: Parent node.
    
        """
>       basename, dirname = key.rsplit(':', 2)
E       AttributeError: 'int' object has no attribute 'rsplit'

pytutils/pytutils/trees.py:53: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_trees_set_tree_node_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""