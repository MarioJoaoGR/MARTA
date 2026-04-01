
import pytest
from docstring_parser.numpydoc import NumpydocParser
from docstring_parser.common import Docstring, DocstringStyle

def test_none_input():
    parser = NumpydocParser()
    result = parser.parse(None)
    
    assert result is not None
    assert result.style == DocstringStyle.NUMPYDOC
