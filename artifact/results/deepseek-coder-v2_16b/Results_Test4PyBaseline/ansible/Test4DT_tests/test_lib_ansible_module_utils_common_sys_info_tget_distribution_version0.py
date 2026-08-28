
import pytest
from ansible.module_utils.common.sys_info import get_distribution_version
from unittest.mock import patch

def test_get_distribution_version_centos():
    with patch('ansible.module_utils.common.sys_info.distro') as mock_distro:
        mock_distro.id.return_value = 'centos'
        mock_distro.version.return_value = '7.5'
        assert get_distribution_version() == '7.5'

def test_get_distribution_version_debian():
    with patch('ansible.module_utils.common.sys_info.distro') as mock_distro:
        mock_distro.id.return_value = 'debian'
        mock_distro.version.return_value = '10'
        assert get_distribution_version() == '10'

def test_get_distribution_version_unknown():
    with patch('ansible.module_utils.common.sys_info.distro') as mock_distro:
        mock_distro.id.return_value = 'unknown'