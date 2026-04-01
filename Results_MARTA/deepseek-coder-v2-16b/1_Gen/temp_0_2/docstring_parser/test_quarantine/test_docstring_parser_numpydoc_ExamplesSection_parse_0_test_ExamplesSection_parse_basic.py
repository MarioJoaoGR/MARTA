
import pytest
from docstring_parser.numpydoc import ExamplesSection, DocstringExample

def test_ExamplesSection_parse_basic():
    section = ExamplesSection()
    examples = list(section.parse(""">>> import numpy.matlib
>>> np.matlib.empty((2, 2))    # filled with random data
matrix([[  6.76425276e-320,   9.79033856e-307], # random
        [  7.39337286e-309,   3.22135945e-309]])
>>> np.matlib.empty((2, 2), dtype=int)
matrix([[ 6600475,        0], # random
        [ 6586976, 22740995]])"""))
    
    assert len(examples) == 2
    for example in examples:
        assert isinstance(example, DocstringExample)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_ExamplesSection_parse_0_test_ExamplesSection_parse_basic
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ExamplesSection_parse_0_test_ExamplesSection_parse_basic.py:6:14: E1120: No value for argument 'title' in constructor call (no-value-for-parameter)
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ExamplesSection_parse_0_test_ExamplesSection_parse_basic.py:6:14: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)


"""