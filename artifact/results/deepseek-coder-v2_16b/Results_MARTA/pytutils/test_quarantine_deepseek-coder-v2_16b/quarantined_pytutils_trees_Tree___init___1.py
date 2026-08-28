
import pytest
from pytutils.trees import Tree



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_valid_initialization ___________________________

    def test_valid_initialization():
        initial = {'a': 1, 'b': 2}
        tree = Tree(initial=initial)
>       assert tree['a'] == 1

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___1.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/trees.py:93: in __getitem__
    return get_tree_node(self, key, default=default)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = Tree(<class 'pytutils.trees.Tree'>, {'a': 1, 'b': 2}), key = ['a']
default = <object object at 0x7f3d19621cb0>, parent = False

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
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___1.py:11: Failed
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___1.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___1.py::test_valid_initialization
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___1.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___1.py::test_invalid_inputs
============================== 3 failed in 0.05s ===============================
"""