
import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.interpreter_discovery import _get_linux_distro

# Test case for valid input with platform_dist_result

# Test case for valid input with osrelease_content
def test_valid_input_with_osrelease_content():
    with patch('ansible.executor.interpreter_discovery._get_linux_distro') as mock_get_linux_distro:
        platform_info = {'osrelease_content': 'ID=Debian\nVERSION_ID="9"'}
        result = _get_linux_distro(platform_info)
        assert result == ('Debian', '9')

# Test case for no input provided
def test_no_input_provided():
    with patch('ansible.executor.interpreter_discovery._get_linux_distro') as mock_get_linux_distro:
        platform_info = {}
        result = _get_linux_distro(platform_info)
        assert result == ('', '')