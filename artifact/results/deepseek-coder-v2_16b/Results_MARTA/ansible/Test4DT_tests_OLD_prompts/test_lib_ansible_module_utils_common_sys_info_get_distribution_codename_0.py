
import pytest
from unittest.mock import patch
from ansible.module_utils.common.sys_info import get_distribution_codename


def test_ubuntu_xenial():
    with patch('platform.system', return_value='Linux'):
        with patch('distro.os_release_info', return_value={'version_codename': 'xenial'}):
            assert get_distribution_codename() == 'xenial'

def test_ubuntu_from_lsb():
    with patch('platform.system', return_value='Linux'):
        with patch('distro.os_release_info', return_value={}):
            with patch('distro.lsb_release_info', return_value={'codename': 'bionic'}):
                assert get_distribution_codename() == 'bionic'

def test_fedora():
    with patch('platform.system', return_value='Linux'):
        with patch('distro.os_release_info', return_value={'version_codename': 'fedora'}):
            assert get_distribution_codename() == 'fedora'
