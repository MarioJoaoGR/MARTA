
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
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree__namespace_key_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_with_namespace ________________________

    def test_valid_input_with_namespace():
        t = Tree({'a': {'b': 1}}, namespace='root')
>       assert t['root:a']['root:b'] == 1

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree__namespace_key_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/trees.py:93: in __getitem__
    return get_tree_node(self, key, default=default)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mapping = Tree(<class 'pytutils.trees.Tree'>, {'a': {'b': 1}})
key = ['root', 'a'], default = <object object at 0x7f54fd2b9c70>, parent = False

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
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        with pytest.raises(TypeError):
>           t = Tree('not a dictionary', namespace='root')

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree__namespace_key_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Tree(<class 'pytutils.trees.Tree'>, {}), initial = 'not a dictionary'
namespace = 'root', initial_is_ref = False

    def __init__(self, initial=None, namespace='', initial_is_ref=False):
        if initial is not None and initial_is_ref:
            self.data = initial_is_ref
        self.namespace = namespace
        super(Tree, self).__init__(self.__class__)
        if initial is not None:
>           self.update(initial)
E           ValueError: dictionary update sequence element #0 has length 1; 2 is required

/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/trees.py:78: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree__namespace_key_0.py::test_valid_input_with_namespace
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_trees_Tree__namespace_key_0.py::test_invalid_input_error_handling
============================== 2 failed in 0.05s ===============================
"""