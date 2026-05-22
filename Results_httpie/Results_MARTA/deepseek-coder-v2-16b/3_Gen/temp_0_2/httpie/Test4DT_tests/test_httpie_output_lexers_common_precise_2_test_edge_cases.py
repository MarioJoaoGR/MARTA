
import pytest
from unittest.mock import patch
from httpie.output.lexers.common import precise

@pytest.mark.parametrize("lexer, precise_token, parent_token, expected", [
    (type('Lexer', (object,), {'options': {}}), None, "DEFAULT_TOKEN", "DEFAULT_TOKEN"),
    (type('Lexer', (object,), {'options': {'precise': True}}), None, "DEFAULT_TOKEN", "DEFAULT_TOKEN"),
    (type('Lexer', (object,), {'options': {'precise': False}}), "CUSTOM_TOKEN", "DEFAULT_TOKEN", "DEFAULT_TOKEN"),
    (type('Lexer', (object,), {'options': {'precise': True}}), "CUSTOM_TOKEN", "DEFAULT_TOKEN", "CUSTOM_TOKEN")
])
def test_edge_cases(lexer, precise_token, parent_token, expected):
    with patch('httpie.output.lexers.common.precise', return_value=expected):
        result = precise(lexer, precise_token, parent_token)
        assert result == expected
