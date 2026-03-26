
import pytest
from docstring_parser.tests.test_numpydoc import parse

@pytest.mark.parametrize("docstring, expected_param_count", [
    ("Short description", 0),
    ("""
    Short description

    Attributes
    ----------
    name
        description 1
    priority : int
        description 2
    sender : str, optional
        description 3
    ratio : Optional[float], optional
        description 4
    """, 4),
    ("""
    Short description

    Attributes
    ----------
    name
        description 1
        with multi-line text
    priority : int
        description 2
    """, 2)
])
def test_invalid_inputs(docstring, expected_param_count):
    docstring = parse(docstring)
    assert len(docstring.params) == expected_param_count
