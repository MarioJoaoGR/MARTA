
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

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
        initial_dict = {'a': 1, 'b': 2}
        t = Tree(initial=initial_dict)
>       assert t['a'] == 1

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/trees.py:93: in __getitem__
    return get_tree_node(self, key, default=default)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = Tree(<class 'pytutils.trees.Tree'>, {'a': 1, 'b': 2}), key = ['a']
default = <object object at 0x7f6dbc49dc80>, parent = False

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
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
        nested_dict = {'sub': {'key': 'value'}}
        t_namespaced = Tree(initial=nested_dict, namespace='root')
>       assert t_namespaced['root:sub']['root:key'] == 'value'

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/trees.py:93: in __getitem__
    return get_tree_node(self, key, default=default)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = Tree(<class 'pytutils.trees.Tree'>, {'sub': {'key': 'value'}})
key = ['root', 'sub'], default = <object object at 0x7f6dbc49dc80>
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
_______________________________ test_error_case ________________________________

    def test_error_case():
        with pytest.raises(ValueError) as excinfo:
            t = Tree(initial='invalid_input')
>       assert str(excinfo.value) == "Invalid initial data provided. Expected a dictionary."
E       AssertionError: assert 'dictionary u...2 is required' == 'Invalid init...a dictionary.'
E         
E         - Invalid initial data provided. Expected a dictionary.
E         + dictionary update sequence element #0 has length 1; 2 is required

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___0.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___0.py::test_valid_case_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___0.py::test_valid_case_2
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree___init___0.py::test_error_case
============================== 3 failed in 0.06s ===============================
"""