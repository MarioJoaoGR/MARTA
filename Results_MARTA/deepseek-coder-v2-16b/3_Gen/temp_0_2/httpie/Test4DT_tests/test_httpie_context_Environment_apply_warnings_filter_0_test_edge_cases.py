
import pytest
from unittest.mock import patch
from httpie.context import Environment, DEFAULT_CONFIG_DIR

@pytest.fixture
def mock_environment():
    return Environment()

def test_edge_cases(mock_environment):
    # Test None values for streams
    mock_environment.stdin = None
    assert mock_environment.stdin is None
    
    mock_environment.stdout = None
    assert mock_environment.stdout is None
    
    mock_environment.stderr = None
    assert mock_environment.stderr is None
    
    # Test empty strings for configurations
    with patch('httpie.context.Environment.config_dir', new=DEFAULT_CONFIG_DIR):
        assert str(mock_environment.config_dir) == str(DEFAULT_CONFIG_DIR)
