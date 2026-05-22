
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.lexers.common import precise

@pytest.mark.parametrize("lexer_options, precise_token, expected", [
    ({}, None, "DEFAULT_TOKEN"),  # No lexer options, no precise token
    ({"precise": True}, "CUSTOM_TOKEN", "CUSTOM_TOKEN"),  # Lexer with precise option enabled and custom token provided
    ({"precise": False}, "CUSTOM_TOKEN", "DEFAULT_TOKEN"),  # Lexer with precise option disabled and no custom token provided
    ({}, None, "DEFAULT_TOKEN"),  # Another test case for the same condition as the first one
])
def test_edge_cases(lexer_options, precise_token, expected):
    lexer = MagicMock()
    lexer.options = lexer_options
    
    with patch('httpie.output.lexers.common.precise', return_value=expected):
        result = precise(lexer, precise_token, "DEFAULT_TOKEN")
        assert result == expected
