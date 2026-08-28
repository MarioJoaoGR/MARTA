
import pytest
from docstring_parser.common import Docstring, DocstringParam, DocstringReturns

# Test 1: Basic Initialization of Docstring
def test_basic_initialization():
    doc = Docstring()
    assert doc is not None, "Docstring instance should be created."

# Test 2: Setting Short Description
def test_set_short_description():
    doc = Docstring()
    doc.short_description = "This function performs a specific task."
    assert doc.short_description == "This function performs a specific task.", "Short description should be set correctly."

# Test 3: Setting Long Description
def test_set_long_description():
    doc = Docstring()
    doc.long_description = "This is a detailed explanation of the function's purpose, parameters, and return values."
    assert doc.long_description == "This is a detailed explanation of the function's purpose, parameters, and return values.", "Long description should be set correctly."

# Test 4: Adding Metadata (Parameters)

# Test 5: Adding Metadata (Returns)
def test_add_metadata_returns():
    doc = Docstring()
    returns_info = DocstringReturns("args", "Description of the return value.", "type_name", True)
    doc.meta.append(returns_info)
    assert len(doc.meta) == 1, "Metadata list should contain one item."
    assert isinstance(doc.meta[0], DocstringReturns), "The first metadata item should be a DocstringReturns instance."

# Test 6: Retrieving Returns Metadata