
import ast
from docstring_parser.attrdoc import ast_is_literal_str, ast_get_constant_value

def test_valid_input():
    # Create an example AST node representing a literal string
    example_node = ast.parse("'Hello, World!'").body[0].value
    
    # Call the function and assert that it returns True for the literal string node
    assert ast_is_literal_str(example_node) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_3_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create an example AST node representing a literal string
        example_node = ast.parse("'Hello, World!'").body[0].value
    
        # Call the function and assert that it returns True for the literal string node
>       assert ast_is_literal_str(example_node) == True
E       assert False == True
E        +  where False = ast_is_literal_str(<ast.Constant object at 0x104980640>)

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_3_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_3_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""