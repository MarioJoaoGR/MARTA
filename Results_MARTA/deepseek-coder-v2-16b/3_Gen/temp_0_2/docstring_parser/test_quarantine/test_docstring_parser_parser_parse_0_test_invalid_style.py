
import pytest
from unittest.mock import patch
from docstring_parser.parser import DocstringStyle, parse, ParseError
from docstring_parser.exceptions import DocstringParseError

@pytest.mark.parametrize("style", [DocstringStyle.AUTO, DocstringStyle.REST])
def test_invalid_style(style):
    with patch('docstring_parser.parser._STYLE_MAP', {style: MockParser()}):
        if style == DocstringStyle.AUTO:
            with pytest.raises(ParseError):
                parse("Invalid docstring", style=DocstringStyle.AUTO)
        else:
            with pytest.raises(ParseError):
                parse("Invalid docstring", style=style)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_parser_parse_0_test_invalid_style
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_0_test_invalid_style.py:5:0: E0401: Unable to import 'docstring_parser.exceptions' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_0_test_invalid_style.py:5:0: E0611: No name 'exceptions' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_0_test_invalid_style.py:9:61: E0602: Undefined variable 'MockParser' (undefined-variable)


"""