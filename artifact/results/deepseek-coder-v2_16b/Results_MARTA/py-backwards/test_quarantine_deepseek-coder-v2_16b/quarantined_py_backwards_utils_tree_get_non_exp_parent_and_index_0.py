
import ast
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
        sample_ast = ast.parse('def example(): pass')
        node = sample_ast.body[0]
>       parent, index = get_non_exp_parent_and_index(sample_ast, node)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:29: in get_non_exp_parent_and_index
    parent = get_parent(tree, node)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7fe77eb2bbb0>
key = <ast.FunctionDef object at 0x7fe77eb5cee0>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7fe77eb6cc70; to 'FunctionDef' at 0x7fe77eb5cee0>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
_________________________ test_valid_case_class_method _________________________

    def test_valid_case_class_method():
        sample_ast = ast.parse('class Example:\n    def example_method(self):\n        pass')
>       node = sample_ast.body[1]
E       IndexError: list index out of range

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py:15: IndexError
______________________ test_valid_case_function_with_body ______________________

    def test_valid_case_function_with_body():
        sample_ast = ast.parse('def example():\n    print("Hello, World!")')
        node = sample_ast.body[0]
>       parent, index = get_non_exp_parent_and_index(sample_ast, node)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:29: in get_non_exp_parent_and_index
    parent = get_parent(tree, node)
/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:21: in get_parent
    return _parents[node]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <WeakKeyDictionary at 0x7fe77eb2bbb0>
key = <ast.FunctionDef object at 0x7fe77f552980>

    def __getitem__(self, key):
>       return self.data[ref(key)]
E       KeyError: <weakref at 0x7fe77eb6fce0; to 'FunctionDef' at 0x7fe77f552980>

/opt/conda/envs/test4py_env/lib/python3.10/weakref.py:416: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py::test_valid_case_simple_function
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py::test_valid_case_class_method
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_get_non_exp_parent_and_index_0.py::test_valid_case_function_with_body
============================== 3 failed in 0.08s ===============================
"""