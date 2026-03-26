
import pytest
from pytutils.trees import Tree, set_tree_node

def test_invalid_input():
    tree = Tree()
    with pytest.raises(TypeError):
        tree[''] = 'value'  # This should raise TypeError because key is empty

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

pytutils/Test4DT_tests/test_pytutils_trees_Tree___setitem___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        tree = Tree()
        with pytest.raises(TypeError):
>           tree[''] = 'value'  # This should raise TypeError because key is empty

pytutils/Test4DT_tests/test_pytutils_trees_Tree___setitem___1_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/trees.py:89: in __setitem__
    return set_tree_node(self, key, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = Tree(<class 'pytutils.trees.Tree'>, {}), key = '', value = 'value'

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
E       ValueError: not enough values to unpack (expected 2, got 1)

pytutils/pytutils/trees.py:53: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_trees_Tree___setitem___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""