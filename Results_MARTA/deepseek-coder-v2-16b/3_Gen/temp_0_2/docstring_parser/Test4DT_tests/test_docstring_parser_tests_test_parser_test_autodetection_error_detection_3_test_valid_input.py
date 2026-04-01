
import pytest
from docstring_parser.tests.test_parser import parse, DocstringStyle, ParseError

def test_autodetection_error_detection() -> None:
    """Test autodection for the case where one of the parsers throws an error
    and another one succeeds.
    """
    source = """
    Does something useless

    :param 3 + 3 a: a param
    """

    with pytest.raises(ParseError):
        # assert that one of the parsers does raise
        parse(source, DocstringStyle.REST)

    # assert that autodetection still works
    docstring = parse(source)

    assert docstring
    assert docstring.style == DocstringStyle.GOOGLE
