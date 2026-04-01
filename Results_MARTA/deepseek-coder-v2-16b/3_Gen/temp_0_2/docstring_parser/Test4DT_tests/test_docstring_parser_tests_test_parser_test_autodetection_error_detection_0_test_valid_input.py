
import pytest
from docstring_parser.tests.test_parser import parse, DocstringStyle, ParseError

def test_valid_input() -> None:
    source = '''\nDoes something useless\n\n:param 3 + 3 a: a param\n'''

    with pytest.raises(ParseError):
        # assert that one of the parsers does raise an error for invalid syntax
        parse(source, DocstringStyle.REST)

    # assert that autodetection still works and correctly identifies Google-style docstrings
    docstring = parse(source)

    assert docstring is not None
    assert docstring.style == DocstringStyle.GOOGLE
