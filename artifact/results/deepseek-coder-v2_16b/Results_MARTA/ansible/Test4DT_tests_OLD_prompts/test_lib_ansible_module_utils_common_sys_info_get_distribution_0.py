
import pytest
from unittest.mock import patch
from ansible.module_utils.common.sys_info import get_distribution



def test_get_distribution_linux_ubuntu():
    with patch('platform.system', return_value='Linux'):
        with patch('distro.id', return_value='ubuntu'):
            assert get_distribution() == 'Ubuntu'

def test_get_distribution_linux_amazon():
    with patch('platform.system', return_value='Linux'):
        with patch('distro.id', return_value='amzn'):
            assert get_distribution() == 'Amazon'

def test_get_distribution_linux_redhat():
    with patch('platform.system', return_value='Linux'):
        with patch('distro.id', return_value='rhel'):
            assert get_distribution() == 'Redhat'
