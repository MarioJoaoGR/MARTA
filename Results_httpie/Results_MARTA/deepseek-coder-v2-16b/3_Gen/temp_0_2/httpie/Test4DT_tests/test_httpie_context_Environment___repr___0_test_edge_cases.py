
import pytest
from unittest.mock import patch
from httpie.context import Environment

@pytest.fixture
def environment():
    return Environment()

def test_environment_repr(environment):
    with patch('httpie.context.sys') as mock_sys:
        # Mocking sys.stdin and sys.stdout for the sake of example
        mock_sys.stdin = None  # Assuming stdin is not available
        mock_sys.stdout = None  # Assuming stdout is not available
        mock_sys.stderr = None  # Assuming stderr is not available
        
        assert repr(environment) == f'<Environment {environment}>'
