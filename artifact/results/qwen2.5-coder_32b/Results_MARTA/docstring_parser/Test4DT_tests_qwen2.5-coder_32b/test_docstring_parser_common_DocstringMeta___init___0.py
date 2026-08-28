
import pytest
from typing import List
from docstring_parser.common import DocstringMeta



def test_valid_inputs():
    """Test that valid inputs are correctly assigned to instance variables."""
    meta = DocstringMeta(["arg1", "arg2"], "This is a description.")
    assert meta.args == ["arg1", "arg2"]
    assert meta.description == "This is a description."

def test_empty_args_list():
    """Test that an empty list for args is correctly assigned to instance variables."""
    meta = DocstringMeta([], "No specific arguments.")
    assert meta.args == []
    assert meta.description == "No specific arguments."

def test_multiple_args():
    """Test that multiple arguments are correctly assigned to instance variables."""
    meta = DocstringMeta(["arg1", "arg2", "arg3"], "Description for multiple args.")
    assert meta.args == ["arg1", "arg2", "arg3"]
    assert meta.description == "Description for multiple args."
