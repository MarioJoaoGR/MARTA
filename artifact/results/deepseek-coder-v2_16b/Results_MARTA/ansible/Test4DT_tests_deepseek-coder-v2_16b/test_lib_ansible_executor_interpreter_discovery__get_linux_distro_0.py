
import pytest
from ansible.executor.interpreter_discovery import _get_linux_distro


def test_valid_input_with_osrelease_content():
    platform_info = {'osrelease_content': 'ID=Debian\nVERSION_ID="9"'}
    result = _get_linux_distro(platform_info)
    assert result == ('Debian', '9')

def test_no_input():
    platform_info = {}
    result = _get_linux_distro(platform_info)
    assert result == (u'', u'')