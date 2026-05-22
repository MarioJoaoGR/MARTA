
import pytest
from httpie.cli.nested_json.parse import tokenize, TokenKind
from unittest.mock import patch

@pytest.fixture(autouse=True)
def setup():
    # Import necessary modules and fixtures here if needed
    pass

def test_none_input():
    with pytest.raises(TypeError):
        list(tokenize(None))
