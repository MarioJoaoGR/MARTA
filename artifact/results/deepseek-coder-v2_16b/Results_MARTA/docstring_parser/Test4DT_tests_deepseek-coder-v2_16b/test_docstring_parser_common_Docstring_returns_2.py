
import pytest
from docstring_parser.common import Docstring, DocstringParam, DocstringReturns

# Test adding parameters to the docstring

# Test retrieving returns information from the docstring

# Test checking for deprecation notice in the docstring
def test_checking_for_deprecation():
    doc = Docstring()
    with pytest.raises(TypeError):
        deprecation_notice = doc.deprecation()