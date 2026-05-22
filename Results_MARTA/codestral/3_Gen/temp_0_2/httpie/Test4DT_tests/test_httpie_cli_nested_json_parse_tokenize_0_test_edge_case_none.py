
import pytest
from httpie.cli.nested_json.parse import tokenize, TokenKind
from unittest.mock import patch

@pytest.fixture(autouse=True)
def mock_tokenize():
    with patch('httpie.cli.nested_json.parse.OPERATORS', {'+': '+'}):
        yield

def test_edge_case_none():
    source = ""
    tokens = list(tokenize(source))
    assert len(tokens) == 0
