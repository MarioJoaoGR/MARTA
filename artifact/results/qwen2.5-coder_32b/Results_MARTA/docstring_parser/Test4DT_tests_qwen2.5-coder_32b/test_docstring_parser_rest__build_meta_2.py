
import pytest
from docstring_parser.rest import _build_meta, DocstringParam


def test__build_meta_param_without_type():
    param_meta = _build_meta(['param', 'verbose'], "If True, prints detailed output.")
    assert isinstance(param_meta, DocstringParam)
    assert param_meta.arg_name == 'verbose'

def test__build_meta_return_with_type():
    return_meta = _build_meta(['return', 'int'], "The sum of two numbers.")
    assert return_meta.type_name == 'int'
    assert return_meta.description == "The sum of two numbers."

def test__build_meta_return_without_type():
    return_meta = _build_meta(['return'], "Returns a boolean value indicating success or failure.")
    assert return_meta.type_name is None
    assert return_meta.description == "Returns a boolean value indicating success or failure."

def test__build_meta_raises_with_type():
    raises_meta = _build_meta(['raises', 'ValueError'], "If the input is out of range.")
    assert raises_meta.type_name == 'ValueError'
    assert raises_meta.description == "If the input is out of range."