
# Module: docstring_parser.tests.test_google
import pytest
from docstring_parser.tests.test_google import parse, DocstringParam  # Corrected import statement

def test_parse_empty_docstring():
    """Test parsing an empty Google-style docstring."""
    docstring = parse("")
    assert len(docstring.params) == 0

def test_parse_short_description_only():
    """Test parsing a short description only in the docstring."""
    docstring = parse("Short description")
    assert len(docstring.params) == 0

def test_parse_with_args():
    """Test parsing multiple arguments in the Google-style docstring."""
    docstring = parse(
        """
        Short description

        Args:
            name: description 1
            priority (int): description 2
            sender (str?): description 3
            ratio (Optional[float], optional): description 4
        """
    )
    assert len(docstring.params) == 4
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "description 1"
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description 2"
    assert not docstring.params[1].is_optional
    assert docstring.params[2].arg_name == "sender"
    assert docstring.params[2].type_name == "str"
    assert docstring.params[2].description == "description 3"
    assert docstring.params[2].is_optional
    assert docstring.params[3].arg_name == "ratio"
    assert docstring.params[3].type_name == "Optional[float]"
    assert docstring.params[3].description == "description 4"
    assert docstring.params[3].is_optional

def test_parse_with_multiline_descriptions():
    """Test parsing arguments with multiline descriptions in the Google-style docstring."""
    docstring = parse(
        """
        Short description

        Args:
            name: description 1
                with multi-line text
            priority (int): description 2
        """
    )
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "name"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == (
        "description 1\nwith multi-line text"
    )
    assert not docstring.params[0].is_optional
    assert docstring.params[1].arg_name == "priority"
    assert docstring.params[1].type_name == "int"
    assert docstring.params[1].description == "description 2"
    assert not docstring.params[1].is_optional

def test_parse_with_invalid_docstring():
    """Test parsing an invalid Google-style docstring."""
    with pytest.raises(ValueError):
        parse("Invalid docstring")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_params_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_params_0.py:4:0: E0611: No name 'DocstringParam' in module 'docstring_parser.tests.test_google' (no-name-in-module)

"""