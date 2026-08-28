
import pytest
from docstring_parser.common import Docstring, DocstringReturns

# Test adding returns to a Docstring object
def test_adding_returns():
    doc = Docstring()
    returns_info = DocstringReturns(None, "Description of the return value", "ReturnType", False)
    doc.meta.append(returns_info)
    assert len(doc.meta) == 1
    assert isinstance(doc.meta[0], DocstringReturns)
    assert doc.meta[0].description == "Description of the return value"
    assert doc.meta[0].type_name == "ReturnType"
    assert not doc.meta[0].is_generator

# Test retrieving returns from a Docstring object