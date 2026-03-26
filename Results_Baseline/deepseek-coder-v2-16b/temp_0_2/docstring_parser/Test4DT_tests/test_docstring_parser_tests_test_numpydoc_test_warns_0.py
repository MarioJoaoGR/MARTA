
from docstring_parser import parse
import pytest

def test_warns():
    """Test parsing warns in a docstring"""
    docstring = parse(
        """
        Short description
        Warns
        -----
        UserWarning: description
        """
    )
    assert len(docstring.meta) == 1, "Expected exactly one meta entry"
    warning = docstring.meta[0]