
import ast
from docstring_parser.attrdoc import ast_get_attribute

def test_valid_input():
    # Example node for testing
    example_node = ast.parse("x = y").body[0]
    
    # Call the function with the example node
    result = ast_get_attribute(example_node)
    
    # Check if the result is as expected
    assert result == ('y', None, None)

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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Example node for testing
        example_node = ast.parse("x = y").body[0]
    
        # Call the function with the example node
        result = ast_get_attribute(example_node)
    
        # Check if the result is as expected
>       assert result == ('y', None, None)
E       AssertionError: assert ('x', None, 'y') == ('y', None, None)
E         
E         At index 0 diff: 'x' != 'y'
E         Use -v to get more diff

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.02s ===============================

"""