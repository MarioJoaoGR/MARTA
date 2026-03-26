
import ast
import pytest
from docstring_parser.attrdoc import ast_is_literal_str, ast_get_constant_value

# Test cases for ast_is_literal_str function
def test_ast_is_literal_str_basic():
    example_node = ast.parse("'Hello, World!'").body[0].value  # Assuming this represents a literal string expression
    assert ast_is_literal_str(example_node) is True

def test_ast_is_literal_str_not_literal():
    tree = ast.parse("1 + 'Hello'")  # This creates an AST with a binary operation and a literal string
    node = tree.body[0].value  # The value of the expression is the second operand, which is a literal string
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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_ast_is_literal_str_basic _________________________

    def test_ast_is_literal_str_basic():
        example_node = ast.parse("'Hello, World!'").body[0].value  # Assuming this represents a literal string expression
>       assert ast_is_literal_str(example_node) is True
E       assert False is True
E        +  where False = ast_is_literal_str(<ast.Constant object at 0x103e01750>)

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_0.py::test_ast_is_literal_str_basic
========================= 1 failed, 1 passed in 0.02s ==========================

"""