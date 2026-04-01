
import ast
from docstring_parser.attrdoc import ast_get_attribute
import typing as T

def test_missing_value_in_annotation_assignment():
    # Create a mock AnnAssign node without a value
    mock_node = ast.AnnAssign(
        target=ast.Name(id='x'),
        annotation=ast.Constant(value='int')
    )
    
    # Call the function and check if it returns None
    result = ast_get_attribute(mock_node)
    assert result is None, "Expected None since there's no value for the annotation"

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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_2_test_missing_value_in_annotation_assignment.py F [100%]

=================================== FAILURES ===================================
_________________ test_missing_value_in_annotation_assignment __________________

    def test_missing_value_in_annotation_assignment():
        # Create a mock AnnAssign node without a value
        mock_node = ast.AnnAssign(
            target=ast.Name(id='x'),
            annotation=ast.Constant(value='int')
        )
    
        # Call the function and check if it returns None
        result = ast_get_attribute(mock_node)
>       assert result is None, "Expected None since there's no value for the annotation"
E       AssertionError: Expected None since there's no value for the annotation
E       assert ('x', "'int'", None) is None

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_2_test_missing_value_in_annotation_assignment.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_2_test_missing_value_in_annotation_assignment.py::test_missing_value_in_annotation_assignment
============================== 1 failed in 0.04s ===============================
"""