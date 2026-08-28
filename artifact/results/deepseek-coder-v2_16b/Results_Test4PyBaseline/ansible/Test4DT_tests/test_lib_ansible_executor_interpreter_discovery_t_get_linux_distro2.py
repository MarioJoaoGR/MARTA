
import pytest
from ansible.executor.interpreter_discovery import _get_linux_distro

# Test cases for _get_linux_distro function

def test_empty_platform_info():
    platform_info = {}
    distro_name, distro_version = _get_linux_distro(platform_info)
    assert (distro_name, distro_version) == ('', '')

def test_invalid_osrelease_content():
    platform_info = {'osrelease_content': 'INVALID CONTENT'}
    distro_name, distro_version = _get_linux_distro(platform_info)
    assert (distro_name, distro_version) == ('', '')

def test_missing_id_in_osrelease():
    platform_info = {'osrelease_content': 'VERSION_ID=20.04'}
    distro_name, distro_version = _get_linux_distro(platform_info)
    assert (distro_name, distro_version) == ('', '20.04')

def test_missing_version_id_in_osrelease():
    platform_info = {'osrelease_content': 'ID=ubuntu'}
    distro_name, distro_version = _get_linux_distro(platform_info)
    assert (distro_name, distro_version) == ('ubuntu', '')

def test_invalid_format_in_osrelease():
    platform_info = {'osrelease_content': 'NAME=Debian\nVERSION="10"'}
    distro_name, distro_version = _get_linux_distro(platform_info)