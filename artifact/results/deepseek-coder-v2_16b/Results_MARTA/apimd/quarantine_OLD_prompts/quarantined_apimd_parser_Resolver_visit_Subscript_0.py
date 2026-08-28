
import pytest
from apimd.parser import Resolver
from astroid.nodes import Subscript, Name, Tuple, Constant, BinOp
from unittest.mock import patch

# Test case for visit_Subscript method with deprecated typing alias
def test_visit_Subscript_with_deprecated_typing_alias():
    resolver = Resolver(root="typing", alias={"Optional": "typing.Optional"})
    ast_node = Subscript(Name('Optional', Load), Tuple([Constant(1), Constant(2)], Load))
    
    with patch('apimd.parser.logger.warning') as mock_warning:
        resolved_ast = resolver.visit_Subscript(ast_node)
        
        assert isinstance(resolved_ast, Subscript)
        assert isinstance(resolved_ast.value, Name)
        assert resolved_ast.value.id == 'typing.Optional'
        mock_warning.assert_called_once_with(f"{ast_node.lineno}:{ast_node.col_offset}: find deprecated name Optional, recommended to use typing.Optional")

# Test case for visit_Subscript method with non-deprecated typing alias
def test_visit_Subscript_without_deprecated_typing_alias():
    resolver = Resolver(root="typing", alias={"List": "typing.List"})
    ast_node = Subscript(Name('List', Load), Tuple([Constant(1), Constant(2)], Load))
    
    with patch('apimd.parser.logger.warning') as mock_warning:
        resolved_ast = resolver.visit_Subscript(ast_node)
        
        assert isinstance(resolved_ast, Subscript)
        assert isinstance(resolved_ast.value, Name)
        assert resolved_ast.value.id == 'typing.List'
        mock_warning.assert_not_called()

# Test case for visit_Subscript method with non-Name value type
def test_visit_Subscript_with_non_name_value():
    resolver = Resolver(root="typing", alias={"Optional": "typing.Optional"})
    ast_node = Subscript(Constant('invalid'), Tuple([Constant(1), Constant(2)], Load))
    
    resolved_ast = resolver.visit_Subscript(ast_node)
    
    assert isinstance(resolved_ast, Subscript)
    assert not isinstance(resolved_ast.value, Name)
    assert resolved_ast == ast_node

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting test_apimd_parser_Resolver_visit_Subscript_0.py _______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Subscript_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Subscript_0.py:4: in <module>
    from astroid.nodes import Subscript, Name, Tuple, Constant, BinOp
E   ImportError: cannot import name 'Constant' from 'astroid.nodes' (/data/pydeps/marta/astroid/nodes/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Resolver_visit_Subscript_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.18s ===============================
"""