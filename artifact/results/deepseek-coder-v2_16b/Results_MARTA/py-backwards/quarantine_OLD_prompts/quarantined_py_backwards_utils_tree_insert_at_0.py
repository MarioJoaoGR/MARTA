
import ast
from typing import List, Union
import pytest
from unittest.mock import patch
from py_backwards.utils.tree import insert_at

@pytest.mark.parametrize("test_input", [
    (0, ast.parse('pass'), ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)),
    (2, ast.parse('pass'), [ast.FunctionDef(name='func1', body=[], lineno=1, col_offset=0), ast.FunctionDef(name='func2', body=[], lineno=2, col_offset=0)]),
    (1, ast.parse('class BaseClass: pass'), ast.ClassDef(name='NewClass', bases=[], keywords=[], body=[], lineno=1, col_offset=0)),
])
def test_insert_at(test_input):
    index, parent, nodes = test_input
    insert_at(index, parent, nodes)
    assert isinstance(parent.body[index], type(nodes))

@pytest.mark.parametrize("test_input", [
    (-1, ast.parse('pass'), ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)),
])
def test_invalid_index(test_input):
    index, parent, nodes = test_input
    with pytest.raises(IndexError):
        insert_at(index, parent, nodes)

@pytest.mark.parametrize("test_input", [
    (0, ast.parse('pass'), 'not a valid AST node'),
])
def test_invalid_nodes(test_input):
    index, parent, nodes = test_input
    with pytest.raises(TypeError):
        insert_at(index, parent, nodes)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py . [ 20%]
F.FF                                                                     [100%]

=================================== FAILURES ===================================
_________________________ test_insert_at[test_input1] __________________________

test_input = (2, <ast.Module object at 0x7fef8d576530>, [<ast.FunctionDef object at 0x7fef8d5765c0>, <ast.FunctionDef object at 0x7fef8d576500>])

    @pytest.mark.parametrize("test_input", [
        (0, ast.parse('pass'), ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)),
        (2, ast.parse('pass'), [ast.FunctionDef(name='func1', body=[], lineno=1, col_offset=0), ast.FunctionDef(name='func2', body=[], lineno=2, col_offset=0)]),
        (1, ast.parse('class BaseClass: pass'), ast.ClassDef(name='NewClass', bases=[], keywords=[], body=[], lineno=1, col_offset=0)),
    ])
    def test_insert_at(test_input):
        index, parent, nodes = test_input
        insert_at(index, parent, nodes)
>       assert isinstance(parent.body[index], type(nodes))
E       AssertionError: assert False
E        +  where False = isinstance(<ast.FunctionDef object at 0x7fef8d5765c0>, <class 'list'>)
E        +    where <class 'list'> = type([<ast.FunctionDef object at 0x7fef8d5765c0>, <ast.FunctionDef object at 0x7fef8d576500>])

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py:16: AssertionError
_______________________ test_invalid_index[test_input0] ________________________

test_input = (-1, <ast.Module object at 0x7fef8d576290>, <ast.FunctionDef object at 0x7fef8d576bc0>)

    @pytest.mark.parametrize("test_input", [
        (-1, ast.parse('pass'), ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)),
    ])
    def test_invalid_index(test_input):
        index, parent, nodes = test_input
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py:23: Failed
_______________________ test_invalid_nodes[test_input0] ________________________

test_input = (0, <ast.Module object at 0x7fef8d576140>, 'not a valid AST node')

    @pytest.mark.parametrize("test_input", [
        (0, ast.parse('pass'), 'not a valid AST node'),
    ])
    def test_invalid_nodes(test_input):
        index, parent, nodes = test_input
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py:31: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py::test_insert_at[test_input1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py::test_invalid_index[test_input0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_insert_at_0.py::test_invalid_nodes[test_input0]
========================= 3 failed, 2 passed in 0.06s ==========================
"""