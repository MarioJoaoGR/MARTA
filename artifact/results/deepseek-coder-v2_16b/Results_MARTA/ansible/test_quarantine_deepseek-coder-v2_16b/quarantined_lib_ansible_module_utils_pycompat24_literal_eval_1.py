
import pytest
from ansible.module_utils.pycompat24 import string_types, text_type, binary_type, integer_types  # Importing required modules
import ast

def literal_eval(node_or_string):
    """
    Safely evaluate an expression node or a string containing a Python literal. The function accepts a single argument, which can be either a string representing a Python literal or an AST (Abstract Syntax Tree) node that represents such a literal. It supports the following Python literal structures: strings, numbers, tuples, lists, dictionaries, booleans, and None.
    
    Parameters:
        node_or_string (str or ast.Expression): The input can be either a string representing a Python literal or an AST node that represents such a literal.
        
    Returns:
        The evaluated Python literal structure as its corresponding native type.
        
    Raises:
        ValueError: If the input string is malformed or contains unsupported constructs.
    """
    _safe_names = {'None': None, 'True': True, 'False': False}
    if isinstance(node_or_string, string_types):
        node_or_string = ast.parse(node_or_string, mode='eval')
    elif not isinstance(node_or_string, ast.Expression):
        raise TypeError("expected AST Expression or string")
    
    def _convert(node):
        if isinstance(node, ast.Const) and isinstance(node.value, (text_type, binary_type, float, complex) + integer_types):
            return node.value
        elif isinstance(node, ast.Tuple):
            return tuple(_convert(n) for n in node.nodes)
        elif isinstance(node, ast.List):
            return list(_convert(n) for n in node.nodes)
        elif isinstance(node, ast.Dict):
            return dict((_convert(k), _convert(v)) for k, v in zip(node.keys, node.values))
        elif isinstance(node, ast.Name):
            if node.name in _safe_names:
                return _safe_names[node.name]
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -_convert(node.operand)  # pylint: disable=invalid-unary-operand-type
        raise ValueError('malformed string')
    
    return _convert(node_or_string.body)

# Test cases for literal_eval function
def test_literal_eval_string():
    assert literal_eval("'hello'") == 'hello'

def test_literal_eval_number():
    assert literal_eval('123') == 123

def test_literal_eval_tuple():
    assert literal_eval('(1, 2, 3)') == (1, 2, 3)

def test_literal_eval_list():
    assert literal_eval('[1, 2, 3]') == [1, 2, 3]

def test_literal_eval_dict():
    assert literal_eval('{"a": 1, "b": 2}') == {'a': 1, 'b': 2}

def test_literal_eval_bool():
    assert literal_eval('True') is True
    assert literal_eval('False') is False

def test_literal_eval_none():
    assert literal_eval('None') is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_lib_ansible_module_utils_pycompat24_literal_eval_1.py __
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_pycompat24_literal_eval_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_pycompat24_literal_eval_1.py:3: in <module>
    from ansible.module_utils.pycompat24 import string_types, text_type, binary_type, integer_types  # Importing required modules
E   ImportError: cannot import name 'string_types' from 'ansible.module_utils.pycompat24' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/pycompat24.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_pycompat24_literal_eval_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.72s ===============================
"""