
import pytest
from thonny.jedi_utils import _copy_of_get_statement_of_position
from parso import python_parser

def create_ast(code):
    parsed = python_parser.parse(code)
    return parsed.children[0]

@pytest.mark.parametrize("code, pos, expected", [
    ("def example(): pass", (1, 4), "FunctionDef"),
    ("if __name__ == '__main__': pass", (2, 0), "IfStmt"),
])
def test_get_statement_of_position(code, pos, expected):
    ast_root = create_ast(code)
    result_node = _copy_of_get_statement_of_position(ast_root, pos)
    
    if expected == "FunctionDef":
        assert result_node.type == expected
    elif expected == "IfStmt":
        assert isinstance(result_node, type(None))  # If no node is found, it should return None

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
/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils__copy_of_get_statement_of_position_0.py:4: in <module>
    from parso import python_parser
E   ImportError: cannot import name 'python_parser' from 'parso' (/data/pydeps/marta/parso/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils__copy_of_get_statement_of_position_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""