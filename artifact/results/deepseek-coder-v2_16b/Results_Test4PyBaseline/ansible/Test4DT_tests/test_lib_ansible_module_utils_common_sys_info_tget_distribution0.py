
import pytest
import platform
import distro
from ansible.module_utils.common.sys_info import get_distribution

# Mock the required functions from the module to simulate different distributions
distro.id = lambda: 'Ubuntu'  # Default mock for testing purposes
platform.system = lambda: 'Linux'  # Ensure platform is Linux

def test_get_distribution_ubuntu():
    distro.id = lambda: 'Ubuntu'
    assert get_distribution() == 'Ubuntu'

def test_get_distribution_amazon():
    distro.id = lambda: 'Amzn'
    assert get_distribution() == 'Amazon'

def test_get_distribution_redhat():
    distro.id = lambda: 'Rhel'
    assert get_distribution() == 'Redhat'

def test_get_distribution_otherlinux():
    distro.id = lambda: None