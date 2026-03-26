
import ast
from docstring_parser.attrdoc import ast_is_literal_str

def test_valid_case():
    """Test if a literal string node is correctly identified."""
    example_node = ast.parse("'Hello, World!'").body[0].value  # Assuming this represents a literal string expression
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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        """Test if a literal string node is correctly identified."""
        example_node = ast.parse("'Hello, World!'").body[0].value  # Assuming this represents a literal string expression
>       assert ast_is_literal_str(example_node) == True
E       assert False == True
E        +  where False = ast_is_literal_str(<ast.Constant object at 0x10638b6a0>)

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_0_test_valid_case.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.03s ===============================
"""