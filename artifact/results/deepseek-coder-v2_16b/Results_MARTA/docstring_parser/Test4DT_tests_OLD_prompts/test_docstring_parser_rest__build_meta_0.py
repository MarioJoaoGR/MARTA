
import pytest
from unittest.mock import patch
from docstring_parser.rest import _build_meta, ParseError
from docstring_parser.common import DocstringMeta, PARAM_KEYWORDS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, RAISES_KEYWORDS


def test_invalid_input_error_handling():
    with pytest.raises(ParseError):
        _build_meta(['param'], 'Invalid input')
