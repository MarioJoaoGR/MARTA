
import ast
from docstring_parser.attrdoc import ast_get_constant_value

def test_none_input():
    node = None  # Test with a None input to simulate no AST node provided
    result = ast_get_constant_value(node)
    assert result is None, f"Expected None but got {result}"

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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_constant_value_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        node = None  # Test with a None input to simulate no AST node provided
>       result = ast_get_constant_value(node)

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_constant_value_1_test_none_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = None

    def ast_get_constant_value(node: ast.AST) -> T.Any:
        """Return the constant's value if the given node is a constant."""
>       return getattr(node, "value")
E       AttributeError: 'NoneType' object has no attribute 'value'

docstring_parser/docstring_parser/attrdoc.py:17: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_constant_value_1_test_none_input.py::test_none_input
============================== 1 failed in 0.03s ===============================
"""