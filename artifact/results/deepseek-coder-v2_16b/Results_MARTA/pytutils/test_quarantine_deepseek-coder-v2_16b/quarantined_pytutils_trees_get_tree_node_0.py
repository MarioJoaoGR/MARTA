
import pytest
from pytutils.trees import get_tree_node



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_get_tree_node_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        mapping = {'a': {'b': {'c': 1}}}
>       assert get_tree_node(mapping, 'a:b:c') == 1

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_get_tree_node_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = {'a': {'b': {'c': 1}}}, key = ['a', 'b', 'c']
default = <object object at 0x7f89ce6e1c70>, parent = False

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
________________________ test_missing_key_with_default _________________________

    def test_missing_key_with_default():
        mapping = {'a': {'b': {'c': 1}}}
>       assert get_tree_node(mapping, 'a:x', default='default_value') == 'default_value'

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_get_tree_node_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = {'a': {'b': {'c': 1}}}, key = ['a', 'x'], default = 'default_value'
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
_______________________ test_missing_key_without_default _______________________

    def test_missing_key_without_default():
        mapping = {'a': {'b': {'c': 1}}}
        with pytest.raises(KeyError):
>           get_tree_node(mapping, 'a:x')

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_get_tree_node_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = {'a': {'b': {'c': 1}}}, key = ['a', 'x']
default = <object object at 0x7f89ce6e1c70>, parent = False

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
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_get_tree_node_0.py::test_valid_input_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_get_tree_node_0.py::test_missing_key_with_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_get_tree_node_0.py::test_missing_key_without_default
============================== 3 failed in 0.06s ===============================
"""