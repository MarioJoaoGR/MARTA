
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

@pytest.fixture
def environment():
    return Environment()

def test_environment_repr(environment):
    with patch('httpie.context.sys') as mock_sys:
        mock_sys.stdin = MagicMock()
        mock_sys.stdout = MagicMock()
        mock_sys.stderr = MagicMock()
        
        # Mock the isatty method to return True for stdin, stdout, and stderr
        mock_sys.stdin.isatty.return_value = True
        mock_sys.stdout.isatty.return_value = True
        mock_sys.stderr.isatty.return_value = True
        
        # Mock the encoding attributes to return None for stdin, stdout, and stderr
        mock_sys.stdin.encoding = None
        mock_sys.stdout.encoding = None
        mock_sys.stderr.encoding = None
        
        expected_repr = f'<Environment {environment}>'
        assert repr(environment) == expected_repr
