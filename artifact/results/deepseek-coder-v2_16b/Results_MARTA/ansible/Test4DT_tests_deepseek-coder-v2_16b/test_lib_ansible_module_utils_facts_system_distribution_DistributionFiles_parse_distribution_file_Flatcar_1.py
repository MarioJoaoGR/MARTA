
import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles
import re

@pytest.fixture(scope="module")
def distro_files():
    return DistributionFiles(module=None)


def test_parse_distribution_file_Flatcar_empty_data(distro_files):
    data = ""
    success, parsed_content = distro_files.parse_distribution_file_Flatcar('os-release', data, '/etc/flatcar/update.conf', {})
    
    assert success is False
    assert not parsed_content

def test_parse_distribution_file_Flatcar_invalid_distro(distro_files):
    data = "GROUP=Ubuntu"
    success, parsed_content = distro_files.parse_distribution_file_Flatcar('os-release', data, '/etc/flatcar/update.conf', {})
    
    assert success is False
    assert not parsed_content