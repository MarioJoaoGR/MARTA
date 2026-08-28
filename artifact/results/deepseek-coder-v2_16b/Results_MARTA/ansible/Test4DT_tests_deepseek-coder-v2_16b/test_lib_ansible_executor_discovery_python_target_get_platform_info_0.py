
import pytest
import platform as py_platform
from unittest.mock import patch, Mock
import os

def get_platform_info():
    result = dict(platform_dist_result=[])

    if hasattr(py_platform, 'dist'):
        result['platform_dist_result'] = py_platform.dist()

    osrelease_content = read_utf8_file('/etc/os-release')
    # try to fall back to /usr/lib/os-release
    if not osrelease_content:
        osrelease_content = read_utf8_file('/usr/lib/os-release')

    result['osrelease_content'] = osrelease_content

    return result

def read_utf8_file(path):
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    return None

# Test scenarios

@pytest.mark.skipif(not hasattr(py_platform, 'dist'), reason="Platform has no dist attribute")
def test_valid_input():
    with patch('builtins.open', Mock(side_effect=FileNotFoundError)):
        result = get_platform_info()
        assert result['osrelease_content'] is None
        assert result['platform_dist_result'] == []

@pytest.mark.skipif(os.path.isfile('/etc/os-release') or os.path.isfile('/usr/lib/os-release'), reason="Files are available")
def test_missing_files():
    with patch('platform.dist', Mock(side_effect=AttributeError)):
        result = get_platform_info()
        assert result['osrelease_content'] is None
        assert result['platform_dist_result'] == []

@pytest.mark.skipif(os.path.isfile('/etc/os-release') or os.path.isfile('/usr/lib/os-release'), reason="Files are available")
def test_platform_dist_missing():
    with patch('builtins.open', Mock(side_effect=FileNotFoundError)):
        result = get_platform_info()
        assert result['osrelease_content'] is None
        assert result['platform_dist_result'] == []
