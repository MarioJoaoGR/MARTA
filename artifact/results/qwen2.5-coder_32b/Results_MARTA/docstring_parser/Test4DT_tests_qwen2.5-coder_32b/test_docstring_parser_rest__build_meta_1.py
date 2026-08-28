
import pytest
from docstring_parser.rest import _build_meta, DocstringParam, DocstringReturns, DocstringRaises, ParseError


def test_happy_path_return():
    return_meta = _build_meta(['return', 'int'], "The sum of two numbers.")
    assert isinstance(return_meta, DocstringReturns)
    assert return_meta.type_name == 'int'

def test_happy_path_raises():
    raises_meta = _build_meta(['raises', 'ValueError'], "If the input is out of range.")
    assert isinstance(raises_meta, DocstringRaises)
    assert raises_meta.type_name == 'ValueError'

def test_param_without_type():
    param_meta_no_type = _build_meta(['param', 'verbose'], "If True, prints detailed output.")
    assert isinstance(param_meta_no_type, DocstringParam)
    assert param_meta_no_type.arg_name == 'verbose'
    assert param_meta_no_type.type_name is None

def test_return_without_type():
    return_meta_no_type = _build_meta(['return'], "Returns a boolean value indicating success or failure.")
    assert isinstance(return_meta_no_type, DocstringReturns)
    assert return_meta_no_type.type_name is None

def test_invalid_param_format():
    with pytest.raises(ParseError):
        _build_meta(['param', 'item_count', 'int?', 'extra_arg'], "The number of items to process. Defaults to 10.")

def test_invalid_return_format():
    with pytest.raises(ParseError):
        _build_meta(['return', 'int', 'extra_arg'], "The sum of two numbers.")

def test_invalid_raises_format():
    with pytest.raises(ParseError):
        _build_meta(['raises', 'ValueError', 'extra_arg'], "If the input is out of range.")