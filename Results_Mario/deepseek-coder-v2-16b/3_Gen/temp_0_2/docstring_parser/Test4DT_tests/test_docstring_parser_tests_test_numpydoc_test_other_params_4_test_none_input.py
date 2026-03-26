
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_none_input():
    """Test handling of None input to check default behavior or error message."""
    # Test with None input
    docstring = parse(None)
    assert not docstring.meta, "Expected no metadata when input is None"

    # Test with a valid docstring string
    docstring_str = """
    Short description
    Other Parameters
    ----------------
    only_seldom_used_keywords : type, optional
        Explanation
    common_parameters_listed_above : type, optional
        Explanation
    """
    docstring = parse(docstring_str)
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args == [
        "other_param",
        "only_seldom_used_keywords",
    ]
    assert docstring.meta[0].arg_name == "only_seldom_used_keywords"
    assert docstring.meta[0].type_name == "type"
    assert docstring.meta[0].is_optional
    assert docstring.meta[0].description == "Explanation"

    assert docstring.meta[1].args == [
        "other_param",
        "common_parameters_listed_above",
    ]
    assert docstring.meta[1].arg_name == "common_parameters_listed_above"
    assert docstring.meta[1].type_name == "type"
    assert docstring.meta[1].is_optional
    assert docstring.meta[1].description == "Explanation"
