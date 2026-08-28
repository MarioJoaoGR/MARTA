
import ast
from typing import List, Union
from unittest.mock import patch
from py_backwards.utils.tree import insert_at

def replace_at(index: int, parent: ast.AST, nodes: Union[ast.AST, List[ast.AST]]) -> None:
    """Replaces the node in the parent's body at the specified index with the provided nodes."""
    if not isinstance(parent, ast.AST):
        raise TypeError("Parent must be an instance of ast.AST")
    if not isinstance(index, int) or index < 0:
        raise TypeError("Index must be a non-negative integer")
    if not (isinstance(nodes, list) and all(isinstance(node, ast.AST) for node in nodes)):
        raise TypeError("Nodes must be a list of AST nodes")
    
    parent.body.pop(index)  # type: ignore
    insert_at(index, parent, nodes)




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_replace_at_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
______________________________ test_valid_replace ______________________________

    def test_valid_replace():
        tree = ast.parse('pass')
        func_def = ast.FunctionDef(name='new_func', body=[], lineno=1, col_offset=0)
        with patch('py_backwards.utils.tree.insert_at') as mock_insert_at:
>           replace_at(index=0, parent=tree, nodes=func_def)

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_replace_at_1.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

index = 0, parent = <ast.Module object at 0x7fe560931b10>
nodes = <ast.FunctionDef object at 0x7fe55ff45ea0>

    def replace_at(index: int, parent: ast.AST, nodes: Union[ast.AST, List[ast.AST]]) -> None:
        """Replaces the node in the parent's body at the specified index with the provided nodes."""
        if not isinstance(parent, ast.AST):
            raise TypeError("Parent must be an instance of ast.AST")
        if not isinstance(index, int) or index < 0:
            raise TypeError("Index must be a non-negative integer")
        if not (isinstance(nodes, list) and all(isinstance(node, ast.AST) for node in nodes)):
>           raise TypeError("Nodes must be a list of AST nodes")
E           TypeError: Nodes must be a list of AST nodes

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_replace_at_1.py:14: TypeError
_____________________________ test_invalid_parent ______________________________

    def test_invalid_parent():
>       with pytest.raises(TypeError):
E       NameError: name 'pytest' is not defined

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_replace_at_1.py:30: NameError
______________________________ test_invalid_index ______________________________

    def test_invalid_index():
        tree = ast.parse('pass')
>       with pytest.raises(TypeError):
E       NameError: name 'pytest' is not defined

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_replace_at_1.py:35: NameError
______________________________ test_invalid_nodes ______________________________

    def test_invalid_nodes():
        tree = ast.parse('pass')
>       with pytest.raises(TypeError):
E       NameError: name 'pytest' is not defined

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_replace_at_1.py:40: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_replace_at_1.py::test_valid_replace
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_replace_at_1.py::test_invalid_parent
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_replace_at_1.py::test_invalid_index
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_tree_replace_at_1.py::test_invalid_nodes
============================== 4 failed in 0.07s ===============================
"""