# Module: docstring_parser.common
import pytest
from typing import List
from docstring_parser.common import DocstringMeta

def test_docstringmeta_initialization():
    # Test with typical parameter description
    param_meta = DocstringMeta(args=['param', 'x'], description='The x coordinate of the point.')
    assert param_meta.args == ['param', 'x']
    assert param_meta.description == 'The x coordinate of the point.'

    # Test with exception description
    raises_meta = DocstringMeta(args=['raises', 'ValueError'], description='If the input is not valid.')
    assert raises_meta.args == ['raises', 'ValueError']
    assert raises_meta.description == 'If the input is not valid.'

    # Test with return value description
    returns_meta = DocstringMeta(args=['return'], description='The result of the computation.')
    assert returns_meta.args == ['return']
    assert returns_meta.description == 'The result of the computation.'

    # Test with custom metadata
    custom_meta = DocstringMeta(args=['custom', 'info'], description='Additional information about the function.')
    assert custom_meta.args == ['custom', 'info']
    assert custom_meta.description == 'Additional information about the function.'

def test_docstringmeta_empty_args():
    # Test with empty args list
    meta = DocstringMeta(args=[], description='No arguments provided.')
    assert meta.args == []
    assert meta.description == 'No arguments provided.'

def test_docstringmeta_single_arg():
    # Test with a single argument
    meta = DocstringMeta(args=['single'], description='Single argument provided.')
    assert meta.args == ['single']
    assert meta.description == 'Single argument provided.'

def test_docstringmeta_no_description():
    # Test with an empty description
    meta = DocstringMeta(args=['param', 'y'], description='')
    assert meta.args == ['param', 'y']
    assert meta.description == ''

def test_docstringmeta_long_description():
    # Test with a long description
    long_desc = "This is a very long description that spans multiple sentences. It provides detailed information about the parameter, including edge cases and potential failure points."
    meta = DocstringMeta(args=['param', 'z'], description=long_desc)
    assert meta.args == ['param', 'z']
    assert meta.description == long_desc
