
import pytest
from docstring_parser.numpydoc import ExamplesSection, DocstringExample

def test_valid_input():
    parser = ExamplesSection()
    text = """
    >>> import numpy as np
    >>> np.empty((2, 2))  # creates an empty matrix
    matrix([[0., 0.], [0., 0.]])
    """
    examples = list(parser.parse(text))
    
    assert len(examples) == 1
    example = examples[0]
    assert isinstance(example, DocstringExample)
    assert example.keys == ['import numpy as np']
    assert example.snippet == 'np.empty((2, 2))'
    assert example.description == 'creates an empty matrix'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_ExamplesSection_parse_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ExamplesSection_parse_0_test_valid_input.py:6:13: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ExamplesSection_parse_0_test_valid_input.py:6:13: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""