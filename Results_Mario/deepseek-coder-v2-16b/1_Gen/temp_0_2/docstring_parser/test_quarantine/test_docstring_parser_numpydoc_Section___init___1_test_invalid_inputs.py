
import pytest
from docstring_parser.numpydoc import Section

def test_invalid_inputs():
    # Test that an error is raised when title is not provided
    with pytest.raises(TypeError):
        Section(key="params")
    
    # Test that an error is raised when key is not provided
    with pytest.raises(TypeError):
        Section(title="Title")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_Section___init___1_test_invalid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_Section___init___1_test_invalid_inputs.py:8:8: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_Section___init___1_test_invalid_inputs.py:12:8: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""