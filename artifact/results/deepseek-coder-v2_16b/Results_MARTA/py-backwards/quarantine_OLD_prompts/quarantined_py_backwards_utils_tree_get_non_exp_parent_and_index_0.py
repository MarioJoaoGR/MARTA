
import ast
from unittest.mock import patch, MagicMock
import pytest
from py_backwards.utils.tree import get_non_exp_parent_and_index



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_valid_case_simple_function ________________________

    def test_valid_case_simple_function():
        sample_ast = ast.parse("def example(): pass")
>       parent_node, index = get_non_exp_parent_and_index(sample_ast, sample_ast.body[0])

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:29: in get_non_exp_parent_and_index
    parent = get_parent(tree, node)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7fdd1dee04f0>
key = <ast.FunctionDef object at 0x7fdd1df5e500>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7fdd1df56e30; to 'FunctionDef' at 0x7fdd1df5e500>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
__________________________ test_edge_case_none_input ___________________________

    def test_edge_case_none_input():
        with pytest.raises(TypeError):
>           get_non_exp_parent_and_index(None, None)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:29: in get_non_exp_parent_and_index
    parent = get_parent(tree, node)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:18: in get_parent
    _build_parents(tree)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:10: in _build_parents
    for node in ast.walk(tree):
/opt/conda/envs/test4py_env/lib/python3.10/site-packages/typed_ast/ast3.py:251: in walk
    todo.extend(iter_child_nodes(node))
/opt/conda/envs/test4py_env/lib/python3.10/site-packages/typed_ast/ast3.py:209: in iter_child_nodes
    for name, field in iter_fields(node):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = None

    def iter_fields(node):
        """
        Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
        that is present on *node*.
        """
>       for field in node._fields:
E       AttributeError: 'NoneType' object has no attribute '_fields'

/opt/conda/envs/test4py_env/lib/python3.10/site-packages/typed_ast/ast3.py:197: AttributeError
______________________ test_invalid_input_error_handling _______________________

    @patch('py_backwards.utils.tree.get_parent', MagicMock(return_value=MagicMock()))
    def test_invalid_input_error_handling():
        sample_ast = ast.parse("pass")
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py:20: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py::test_valid_case_simple_function
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py::test_edge_case_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py::test_invalid_input_error_handling
============================== 3 failed in 0.08s ===============================
"""