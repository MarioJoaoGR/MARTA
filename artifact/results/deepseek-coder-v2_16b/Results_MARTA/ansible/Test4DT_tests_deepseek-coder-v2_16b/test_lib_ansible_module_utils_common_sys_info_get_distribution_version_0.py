
import pytest
from unittest.mock import patch
from ansible.module_utils.common.sys_info import get_distribution_version



def test_get_distribution_version_centos():
    with patch('distro.id', return_value='centos'):
        with patch('distro.version', return_value='7.5'):
            assert get_distribution_version() == '7.5'

def test_get_distribution_version_debian():
    with patch('distro.id', return_value='debian'):
        with patch('distro.version', return_value='10'):
            assert get_distribution_version() == '10'