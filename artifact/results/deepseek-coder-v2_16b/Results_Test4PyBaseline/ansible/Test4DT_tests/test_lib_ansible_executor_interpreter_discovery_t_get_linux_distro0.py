
import pytest
from ansible.executor.interpreter_discovery import _get_linux_distro

# Test cases for _get_linux_distro function

def test_valid_osrelease_content():
    platform_info = {'osrelease_content': 'ID=ubuntu\nVERSION_ID=20.04'}
    distro_name, distro_version = _get_linux_distro(platform_info)
    assert (distro_name, distro_version) == ('ubuntu', '20.04')

def test_missing_osrelease_content():
    platform_info = {}
    distro_name, distro_version = _get_linux_distro(platform_info)
    assert (distro_name, distro_version) == ('', '')

def test_different_distribution():
    platform_info = {'osrelease_content': 'ID=debian\nVERSION_ID=10'}
    distro_name, distro_version = _get_linux_distro(platform_info)
    assert (distro_name, distro_version) == ('debian', '10')

def test_different_format():
    platform_info = {'osrelease_content': 'NAME=Debian\nVERSION="10"'}
    distro_name, distro_version = _get_linux_distro(platform_info)