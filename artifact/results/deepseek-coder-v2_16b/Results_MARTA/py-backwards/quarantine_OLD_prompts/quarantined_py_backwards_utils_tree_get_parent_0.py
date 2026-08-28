
import ast
import pytest
from unittest.mock import patch
from py_backwards.utils.tree import get_parent, _parents, NodeNotFound, _build_parents



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_get_parent_basic _____________________________

    def test_get_parent_basic():
        sample_ast = ast.parse("def example(): pass")
        with patch('py_backwards.utils.tree._build_parents', return_value=None):
>           parent_node = get_parent(sample_ast, sample_ast.body[0])

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7f07182449a0>
key = <ast.FunctionDef object at 0x7f0718247a90>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7f0718292f20; to 'FunctionDef' at 0x7f0718247a90>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
___________________________ test_get_parent_rebuild ____________________________

    def test_get_parent_rebuild():
        sample_ast = ast.parse("def example(): pass")
        with patch('py_backwards.utils.tree._build_parents', return_value=None):
>           parent_node = get_parent(sample_ast, sample_ast.body[0], rebuild=True)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7f07182449a0>
key = <ast.FunctionDef object at 0x7f0718247e50>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7f071809c8b0; to 'FunctionDef' at 0x7f0718247e50>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
_________________________ test_get_parent_nonexistent __________________________

    def test_get_parent_nonexistent():
        sample_ast = ast.parse("def example(): pass")
        with pytest.raises(NodeNotFound):
>           get_parent(sample_ast, ast.Name(id='non_existent_node', ctx=ast.Load()))

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7f07182449a0>
key = <ast.Name object at 0x7f071835f340>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7f0718158f90; to 'Name' at 0x7f071835f340>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py::test_get_parent_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py::test_get_parent_rebuild
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py::test_get_parent_nonexistent
============================== 3 failed in 0.09s ===============================
"""