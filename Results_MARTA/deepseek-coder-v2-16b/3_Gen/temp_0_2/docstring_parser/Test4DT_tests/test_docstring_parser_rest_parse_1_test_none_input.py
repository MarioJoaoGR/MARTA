
import pytest
from docstring_parser.rest import parse, Docstring, DocstringStyle, ParseError

def test_none_input():
    # Test when the input is None
    result = parse(None)
    assert isinstance(result, Docstring)
    assert result.style == DocstringStyle.REST
    assert result.short_description is None
    assert result.long_description is None
    assert len(result.meta) == 0
