
import pytest
from unittest.mock import MagicMock, patch
import sys
import platform
from httpie.core import print_debug_info

@pytest.fixture(autouse=True)
def mock_environment():
    env = MagicMock()
    with patch('httpie.core.sys', autospec=True):
        yield env

def test_invalid_environment(mock_environment):
    # Call the function with the mocked environment
    print_debug_info(mock_environment)
    
    # Assert that stderr is called with expected content
    mock_environment.stderr.writelines.assert_called()
