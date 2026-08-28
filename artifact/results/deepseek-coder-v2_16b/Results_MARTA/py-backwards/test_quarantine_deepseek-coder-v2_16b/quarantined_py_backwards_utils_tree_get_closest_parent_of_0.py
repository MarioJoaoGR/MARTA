
import ast
import pytest
from py_backwards.utils.tree import get_closest_parent_of, NodeNotFound



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_closest_parent_of_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        sample_ast = ast.parse('def example(): pass')
>       closest_parent = get_closest_parent_of(sample_ast, sample_ast.body[0], ast.FunctionDef)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_closest_parent_of_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:71: in get_closest_parent_of
    parent = get_parent(tree, parent)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7fcc48a67af0>
key = <ast.FunctionDef object at 0x7fcc48a74070>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7fcc48aa09a0; to 'FunctionDef' at 0x7fcc48a74070>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(NodeNotFound):
>           get_closest_parent_of(None, None, ast.FunctionDef)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_closest_parent_of_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:71: in get_closest_parent_of
    parent = get_parent(tree, parent)
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
______________________________ test_missing_type _______________________________

    def test_missing_type():
        sample_ast = ast.parse('def example(): pass')
        try:
>           closest_parent = get_closest_parent_of(sample_ast, sample_ast.body[0], ast.FunctionDef)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_closest_parent_of_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:71: in get_closest_parent_of
    parent = get_parent(tree, parent)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7fcc48a67af0>
key = <ast.FunctionDef object at 0x7fcc488dfb50>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7fcc48aa34c0; to 'FunctionDef' at 0x7fcc488dfb50>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_closest_parent_of_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_closest_parent_of_0.py::test_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_closest_parent_of_0.py::test_missing_type
============================== 3 failed in 0.08s ===============================
"""