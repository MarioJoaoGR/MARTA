
import pytest
from httpie.cli.nested_json.parse import parse, PathAction, TokenKind, NestedJSONSyntaxError
from unittest.mock import patch

def test_edge_case():
    with patch('httpie.cli.nested_json.parse.LITERAL_TOKENS', [TokenKind.TEXT]):
        with pytest.raises(NestedJSONSyntaxError):
            list(parse("root['key']path"))
