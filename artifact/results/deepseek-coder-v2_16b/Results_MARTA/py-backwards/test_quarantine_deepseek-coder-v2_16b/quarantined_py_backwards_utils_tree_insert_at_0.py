
import ast
from typing import List, Union
import pytest
from py_backwards.utils.tree import insert_at





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
________________________ test_error_case_invalid_index _________________________

    def test_error_case_invalid_index():
        tree = ast.parse('pass')
        func_def = ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)
    
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py:11: Failed
________________________ test_error_case_invalid_parent ________________________

    def test_error_case_invalid_parent():
        func_def = ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)
    
        with pytest.raises(TypeError):
>           insert_at(index=0, parent='not_an_ast', nodes=func_def)  # Invalid parent type

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

index = 0, parent = 'not_an_ast'
nodes = [<ast.FunctionDef object at 0x7f578aba7c10>]

    def insert_at(index: int, parent: ast.AST,
                  nodes: Union[ast.AST, List[ast.AST]]) -> None:
        """Inserts nodes to parents body at index."""
        if not isinstance(nodes, list):
            nodes = [nodes]
    
        for child in nodes[::-1]:
>           parent.body.insert(index, child)  # type: ignore
E           AttributeError: 'str' object has no attribute 'body'

/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/tree.py:55: AttributeError
________________________ test_error_case_invalid_nodes _________________________

    def test_error_case_invalid_nodes():
        tree = ast.parse('pass')
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py:23: Failed
___________________________ test_insert_single_node ____________________________

    def test_insert_single_node():
        tree = ast.parse('pass')
        func_def = ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)
    
        insert_at(index=0, parent=tree, nodes=func_def)
>       assert len(tree.body) == 1
E       assert 2 == 1
E        +  where 2 = len([<ast.FunctionDef object at 0x7f578abe36d0>, <ast.Pass object at 0x7f578abe0550>])
E        +    where [<ast.FunctionDef object at 0x7f578abe36d0>, <ast.Pass object at 0x7f578abe0550>] = <ast.Module object at 0x7f578abe3700>.body

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py:31: AssertionError
__________________________ test_insert_multiple_nodes __________________________

    def test_insert_multiple_nodes():
        tree = ast.parse('pass')
        func_def1 = ast.FunctionDef(name='func1', body=[], lineno=1, col_offset=0)
        func_def2 = ast.FunctionDef(name='func2', body=[], lineno=1, col_offset=0)
    
        insert_at(index=0, parent=tree, nodes=[func_def1, func_def2])
>       assert len(tree.body) == 2
E       assert 3 == 2
E        +  where 3 = len([<ast.FunctionDef object at 0x7f578ab434c0>, <ast.FunctionDef object at 0x7f578ab43160>, <ast.Pass object at 0x7f578ab42d10>])
E        +    where [<ast.FunctionDef object at 0x7f578ab434c0>, <ast.FunctionDef object at 0x7f578ab43160>, <ast.Pass object at 0x7f578ab42d10>] = <ast.Module object at 0x7f578ab42ec0>.body

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py:39: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py::test_error_case_invalid_index
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py::test_error_case_invalid_parent
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py::test_error_case_invalid_nodes
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py::test_insert_single_node
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py::test_insert_multiple_nodes
============================== 5 failed in 0.06s ===============================
"""