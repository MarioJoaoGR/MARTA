
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.lexers.common import precise

@pytest.mark.parametrize("lexer_precise, precise_token, expected", [
    (True, "CUSTOM_TOKEN", "CUSTOM_TOKEN"),
    (False, "CUSTOM_TOKEN", "DEFAULT_TOKEN"),
    (None, "CUSTOM_TOKEN", "DEFAULT_TOKEN"),
    (True, None, "DEFAULT_TOKEN"),
    (False, None, "DEFAULT_TOKEN")
])
def test_edge_case_none(lexer_precise, precise_token, expected):
    lexer = MagicMock()
    lexer.options = {"precise": lexer_precise}
    parent_token = "DEFAULT_TOKEN"
    
    with patch('httpie.output.lexers.common.precise', return_value=expected):
        result = precise(lexer, precise_token, parent_token)
        assert result == expected
