
import pytest
from docstring_parser.tests.test_rest import parse
from docstring_parser.common import ParseError

def test_invalid_inputs() -> None:
    """Test invalid inputs to check error handling."""
    # Test with an empty docstring
    docstring = parse("")
    assert len(docstring.params) == 0
    
    # Test with a malformed docstring (missing colon after parameter name)
    with pytest.raises(ParseError):
        docstring = parse(
            """
            Short description
    
            :param name description 1
            :param int priority: description 2
            :param str? sender: description 3
            :param str? message: description 4, defaults to 'hello'
            :param str? multiline: long description 5,
            defaults to 'bye'
            """
        )
