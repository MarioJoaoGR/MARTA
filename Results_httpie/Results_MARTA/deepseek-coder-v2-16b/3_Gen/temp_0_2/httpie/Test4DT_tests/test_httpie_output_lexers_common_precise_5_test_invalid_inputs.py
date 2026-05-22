
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.lexers.common import precise

@pytest.fixture(autouse=True)
def mock_lexer():
    lexer = type('Lexer', (object,), {'options': {'precise': True}})
    yield lexer

@patch('httpie.output.lexers.common.precise')
def test_invalid_inputs(mock_precise):
    # Arrange
    mock_lexer = MagicMock()
    mock_lexer.options.get.return_value = False  # Ensure 'precise' is disabled
    
    # Act
    result1 = precise(mock_lexer, "CUSTOM_TOKEN", "DEFAULT_TOKEN")
    result2 = precise(mock_lexer, None, "DEFAULT_TOKEN")
    
    # Assert
    assert result1 == "DEFAULT_TOKEN"
    assert result2 == "DEFAULT_TOKEN"
