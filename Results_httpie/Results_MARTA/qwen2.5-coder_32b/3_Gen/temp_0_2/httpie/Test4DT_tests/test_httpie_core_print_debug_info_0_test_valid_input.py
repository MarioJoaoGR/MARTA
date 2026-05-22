
import pytest
from unittest.mock import patch, MagicMock
from httpie.core import print_debug_info

@pytest.fixture(autouse=True)
def mock_environment():
    with patch('httpie.core.sys') as sys_mock, \
         patch('httpie.core.platform') as platform_mock, \
         patch('httpie.core.plugin_manager') as plugin_manager_mock:
        env = MagicMock()
        yield env, sys_mock, platform_mock, plugin_manager_mock

def test_print_debug_info(mock_environment):
    env, sys_mock, platform_mock, plugin_manager_mock = mock_environment
    
    # Mock the necessary attributes and versions for testing
    httpie_version = "0.9.9"
    requests_version = "2.25.1"
    pygments_version = "2.7.4"
    sys_mock.version = "3.8.5"
    sys_mock.executable = "/usr/bin/python3"
    platform_mock.system.return_value = "Linux"
    platform_mock.release.return_value = "5.4.0-123-generic"
    
    # Call the function with the mocked environment
    print_debug_info(env)
    
    # Add assertions to verify the output or behavior if needed
    env.stderr.writelines.assert_called()  # Example assertion
