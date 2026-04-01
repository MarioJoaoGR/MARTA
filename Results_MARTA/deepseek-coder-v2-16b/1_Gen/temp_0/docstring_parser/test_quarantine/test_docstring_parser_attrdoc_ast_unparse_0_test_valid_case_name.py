
import ast
from unittest.mock import patch
import pytest
from docstring_parser.attrdoc import ast_unparse

@pytest.mark.parametrize("node", [
    ast.Constant(value=1),
    ast.Name(id='x'),
])
def test_valid_case_name(node):
    with patch('docstring_parser.attrdoc.ast_get_constant_value', return_value=node.id if isinstance(node, ast.Name) else None):
        result = ast_unparse(node)
        expected_result = node.id if isinstance(node, ast.Name) else None
        assert result == expected_result

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_unparse_0_test_valid_case_name.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_case_name[node0] __________________________

node = <ast.Constant object at 0x10299bc10>

    @pytest.mark.parametrize("node", [
        ast.Constant(value=1),
        ast.Name(id='x'),
    ])
    def test_valid_case_name(node):
        with patch('docstring_parser.attrdoc.ast_get_constant_value', return_value=node.id if isinstance(node, ast.Name) else None):
            result = ast_unparse(node)
            expected_result = node.id if isinstance(node, ast.Name) else None
>           assert result == expected_result
E           AssertionError: assert '1' == None

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_unparse_0_test_valid_case_name.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_unparse_0_test_valid_case_name.py::test_valid_case_name[node0]
========================= 1 failed, 1 passed in 0.03s ==========================

"""