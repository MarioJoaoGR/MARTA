
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_other_params() -> None:
    """Test parsing other parameters in a numpy-style docstring."""
    docstring = parse(
        """
        Short description
        Other Parameters
        ----------------
        only_seldom_used_keywords : type, optional
            Explanation
        common_parameters_listed_above : type, optional
            Explanation
        """
    )
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
