
import ast
from docstring_parser.attrdoc import ast_get_attribute

def test_valid_input_attribute_assignment():
    """Test if the function correctly parses an attribute assignment node."""
    # Example AST node for a simple attribute assignment
    example_node = ast.Assign(
        targets=[ast.Name(id='example_attr')],
        value=ast.Constant(value='default_value')
    )
    
    result = ast_get_attribute(example_node)
    assert result == ('example_attr', None, 'default_value')

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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_2_test_valid_input_attribute_assignment.py F [100%]

=================================== FAILURES ===================================
____________________ test_valid_input_attribute_assignment _____________________

    def test_valid_input_attribute_assignment():
        """Test if the function correctly parses an attribute assignment node."""
        # Example AST node for a simple attribute assignment
        example_node = ast.Assign(
            targets=[ast.Name(id='example_attr')],
            value=ast.Constant(value='default_value')
        )
    
        result = ast_get_attribute(example_node)
>       assert result == ('example_attr', None, 'default_value')
E       assert ('example_att...fault_value'") == ('example_att...efault_value')
E         
E         At index 2 diff: "'default_value'" != 'default_value'
E         Use -v to get more diff

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_2_test_valid_input_attribute_assignment.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_2_test_valid_input_attribute_assignment.py::test_valid_input_attribute_assignment
============================== 1 failed in 0.04s ===============================
"""