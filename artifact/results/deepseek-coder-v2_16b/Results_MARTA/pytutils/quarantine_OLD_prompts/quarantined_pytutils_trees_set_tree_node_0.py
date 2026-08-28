
import pytest
from pytutils.trees import set_tree_node, get_tree_node


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_set_tree_node_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        mapping = {'a': {}}
        key = 'a:b'
        value = 1
>       set_tree_node(mapping, key, value)

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_set_tree_node_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/trees.py:54: in set_tree_node
    parent_node = get_tree_node(mapping, dirname)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = {'a': {}}, key = ['b'], default = <object object at 0x7f831622dcb0>
parent = False

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

/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/trees.py:27: AttributeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        mapping = {'a': {}}
        key = 123
        value = None
        with pytest.raises(TypeError):
>           set_tree_node(mapping, key, value)

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_set_tree_node_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = {'a': {}}, key = 123, value = None

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

/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/trees.py:53: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_set_tree_node_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_set_tree_node_0.py::test_invalid_input
============================== 2 failed in 0.05s ===============================
"""