
import ast
import pytest
from py_backwards.utils.tree import get_parent, NodeNotFound



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
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        sample_ast = ast.parse('def example(): pass')
>       parent_node = get_parent(sample_ast, sample_ast.body[0])

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7fc4d1cfbaf0>
key = <ast.FunctionDef object at 0x7fc4d1d30c10>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7fc4d1d38680; to 'FunctionDef' at 0x7fc4d1d30c10>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
______________________________ test_rebuild_true _______________________________

    def test_rebuild_true():
        sample_ast = ast.parse('def example(): pass')
>       parent_node = get_parent(sample_ast, sample_ast.body[0], rebuild=True)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7fc4d1cfbaf0>
key = <ast.FunctionDef object at 0x7fc4d2712710>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7fc4d1d6c8b0; to 'FunctionDef' at 0x7fc4d2712710>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        sample_ast = ast.parse('def example(): pass')
        with pytest.raises(NodeNotFound):
>           parent_node = get_parent(sample_ast, ast.Name(id='non_existent_node', ctx=ast.Load()))

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7fc4d1cfbaf0>
key = <ast.Name object at 0x7fc4d1e276a0>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7fc4d1bd8270; to 'Name' at 0x7fc4d1e276a0>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py::test_rebuild_true
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_parent_0.py::test_invalid_input
============================== 3 failed in 0.08s ===============================
"""