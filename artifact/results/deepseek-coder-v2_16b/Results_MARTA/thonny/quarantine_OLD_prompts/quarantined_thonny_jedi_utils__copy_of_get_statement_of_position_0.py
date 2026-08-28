
import pytest
from unittest.mock import patch
from thonny.jedi_utils import _copy_of_get_statement_of_position
from parso import python_parser

# Test 1: Basic Usage with Parsed AST
def test_basic_usage():
    parsed = python_parser.parse("def example(): pass")
    ast_root = parsed.children[0]
    target_pos = (1, 4)
    result_node = _copy_of_get_statement_of_position(ast_root, target_pos)
    assert result_node is not None, "Expected a node to be found at position (1, 4)"
    assert result_node.type == "FunctionDef", f"Unexpected node type: {result_node.type}"

# Test 2: Usage with a Different AST
def test_usage_with_different_ast():
    parsed = python_parser.parse("if __name__ == '__main__': pass")
    ast_root = parsed.children[0]
    target_pos = (2, 0)
    result_node = _copy_of_get_statement_of_position(ast_root, target_pos)
    assert result_node is not None, "Expected a node to be found at position (2, 0)"
    assert result_node.type == "If", f"Unexpected node type: {result_node.type}"

# Test 3: Usage with a Custom AST
def test_usage_with_custom_ast():
    class CustomNode:
        def __init__(self, type, start_pos, end_pos):
            self.type = type
            self.start_pos = start_pos
            self.end_pos = end_pos
            self.children = []

    ast_root = CustomNode("Module", (0, 0), (10, 0))
    func_def_node = CustomNode("FunctionDef", (1, 2), (5, 2))
    ast_root.children.append(func_def_node)

    target_pos = (3, 4)
    result_node = _copy_of_get_statement_of_position(ast_root, target_pos)
    assert result_node is not None, "Expected a node to be found at position (3, 4)"
    assert result_node.type == "FunctionDef", f"Unexpected node type: {result_node.type}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_thonny_jedi_utils__copy_of_get_statement_of_position_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils__copy_of_get_statement_of_position_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils__copy_of_get_statement_of_position_0.py:5: in <module>
    from parso import python_parser
E   ImportError: cannot import name 'python_parser' from 'parso' (/data/pydeps/marta/parso/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils__copy_of_get_statement_of_position_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""