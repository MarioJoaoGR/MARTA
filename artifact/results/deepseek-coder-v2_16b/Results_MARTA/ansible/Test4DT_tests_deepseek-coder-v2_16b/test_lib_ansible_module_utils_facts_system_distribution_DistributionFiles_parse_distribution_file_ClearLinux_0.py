
import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles
import re

@pytest.fixture(scope="function")
def distro_files():
    return DistributionFiles(module='test')

def test_valid_case(distro_files):
    mock_os_release = """NAME="Clear Linux"
VERSION_ID=34567
ID=clearlinux"""
    
    with pytest.raises(TypeError):
        success, clear_facts = distro_files.parse_distribution_file_ClearLinux('clearlinux', None, '/etc/os-release', collected_facts={})


def test_error_case(distro_files):
    mock_os_release = """NAME="Ubuntu"
VERSION_ID=20.04
ID=ubuntu"""
    
    with pytest.raises(TypeError):
        success, clear_facts = distro_files.parse_distribution_file_ClearLinux('clearlinux', None, '/etc/os-release', collected_facts={})