
import pytest
from docstring_parser.common import DocstringMeta

# Test initialization with valid arguments
def test_init_with_valid_arguments():
    meta = DocstringMeta(args=["arg1", "arg2"], description="This is a test")
    assert meta.args == ["arg1", "arg2"]
    assert meta.description == "This is a test"

# Test initialization with None arguments
def test_init_with_none_arguments():
    meta = DocstringMeta(args=None, description="This is a test")
    assert meta.args is None
    assert meta.description == "This is a test"

# Test initialization with empty list argument
def test_init_with_empty_list_argument():
    meta = DocstringMeta(args=[], description="This is a test")
    assert meta.args == []
    assert meta.description == "This is a test"

# Test initialization without description
def test_init_without_description():
    meta = DocstringMeta(args=["arg1", "arg2"], description=None)
    assert meta.args == ["arg1", "arg2"]