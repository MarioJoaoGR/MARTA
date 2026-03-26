
import pytest
from pytutils.trees import get_tree_node

def set_tree_node(mapping, key, value):
    """
    Set an item in the object with optional namespace handling.

    This method allows setting a value at a specified key within the object, 
    optionally within a given namespace. It uses a helper function `set_tree_node` to perform the actual setting operation.

    Parameters:
        mapping (collections.Mapping): Mapping to fetch from and update.
        key (str|unicode): Key to set, allowing for : notation to traverse deeper into the nested structure.
        value (str|unicode): Value to set at the specified key.

    Returns:
        object: The parent node of the newly set key-value pair.

    Examples:
        >>> mapping = {'a': {'b': {}}}
        >>> set_tree_node(mapping, 'a:b:c', 1)
        {'c': 1}
        >>> print(mapping)
        {'a': {'b': {'c': 1}}}
        
        Setting a value at the root level:
        >>> mapping = {}
        >>> set_tree_node(mapping, 'a:b', 2)
        {'b': 2}
        >>> print(mapping)
        {'a': {'b': 2}}
    """
    basename, dirname = key.rsplit(':', 2)
    parent_node = get_tree_node(mapping, dirname)
    parent_node[basename] = value
    return parent_node

def test_missing_key():
    mapping = {}
    set_tree_node(mapping, 'a:b:c', 1)
    assert mapping == {'a': {'b': {'c': 1}}}
    
    # Test setting a value at the root level
    mapping = {}
    set_tree_node(mapping, 'a:b', 2)
    assert mapping == {'a': {'b': 2}}

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

pytutils/Test4DT_tests/test_pytutils_trees_set_tree_node_0_test_missing_key.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_missing_key _______________________________

    def test_missing_key():
        mapping = {}
>       set_tree_node(mapping, 'a:b:c', 1)

pytutils/Test4DT_tests/test_pytutils_trees_set_tree_node_0_test_missing_key.py:41: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = {}, key = 'a:b:c', value = 1

    def set_tree_node(mapping, key, value):
        """
        Set an item in the object with optional namespace handling.
    
        This method allows setting a value at a specified key within the object,
        optionally within a given namespace. It uses a helper function `set_tree_node` to perform the actual setting operation.
    
        Parameters:
            mapping (collections.Mapping): Mapping to fetch from and update.
            key (str|unicode): Key to set, allowing for : notation to traverse deeper into the nested structure.
            value (str|unicode): Value to set at the specified key.
    
        Returns:
            object: The parent node of the newly set key-value pair.
    
        Examples:
            >>> mapping = {'a': {'b': {}}}
            >>> set_tree_node(mapping, 'a:b:c', 1)
            {'c': 1}
            >>> print(mapping)
            {'a': {'b': {'c': 1}}}
    
            Setting a value at the root level:
            >>> mapping = {}
            >>> set_tree_node(mapping, 'a:b', 2)
            {'b': 2}
            >>> print(mapping)
            {'a': {'b': 2}}
        """
>       basename, dirname = key.rsplit(':', 2)
E       ValueError: too many values to unpack (expected 2)

pytutils/Test4DT_tests/test_pytutils_trees_set_tree_node_0_test_missing_key.py:34: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_trees_set_tree_node_0_test_missing_key.py::test_missing_key
============================== 1 failed in 0.05s ===============================
"""