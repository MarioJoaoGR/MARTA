
# Module: docstring_parser.rest
import pytest
from docstring_parser import _build_meta, ParseError
from docstring_parser.rest import (
    DocstringMeta,
    DocstringParam,
    DocstringReturns,
    DocstringDeprecated,
    DocstringRaises,
)

# Test cases for _build_meta function
def test_build_meta_param():
    meta = _build_meta(["param", "arg1", "int"], "This parameter is used to pass argument one.")
    assert isinstance(meta, DocstringParam)
    assert meta.args == ["param", "arg1", "int"]
    assert meta.description == "This parameter is used to pass argument one."
    assert meta.arg_name == "arg1"
    assert meta.type_name == "int"
    assert meta.is_optional is None
    assert meta.default is None

def test_build_meta_returns():
    meta = _build_meta(["returns", "result"], "The function returns a result object.")
    assert isinstance(meta, DocstringReturns)
    assert meta.args == ["returns", "result"]
    assert meta.description == "The function returns a result object."
    assert meta.type_name == "result"
    assert meta.is_generator is False

def test_build_meta_deprecate():
    meta = _build_meta(["deprecate", "old_arg"], "Use new_arg instead, available from version v2.0.")
    assert isinstance(meta, DocstringDeprecated)
    assert meta.args == ["deprecate", "old_arg"]
    assert meta.version == "v2.0"
    assert meta.description == "Use new_arg instead, available from version v2.0."

def test_build_meta_raises():
    meta = _build_meta(["raises", "ValueError"], "An error is raised if the input value is invalid.")
    assert isinstance(meta, DocstringRaises)
    assert meta.args == ["raises", "ValueError"]
    assert meta.description == "An error is raised if the input value is invalid."
    assert meta.type_name == "ValueError"

def test_build_meta_invalid_keyword():
    with pytest.raises(ParseError):
        _build_meta(["unknown", "arg1"], "This should raise an error.")

def test_build_meta_missing_arguments():
    with pytest.raises(ParseError):
        _build_meta([], "Expected one or two arguments for a param keyword.")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest__build_meta_0
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0.py:4:0: E0611: No name '_build_meta' in module 'docstring_parser' (no-name-in-module)

"""