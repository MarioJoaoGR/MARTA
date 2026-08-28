
import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles
import re

@pytest.fixture
def distro_files():
    return DistributionFiles(module='my_app')

def test_valid_input_parse_distribution_file_Amazon(distro_files):
    data = 'VERSION_ID="1.0"'
    path = '/etc/os-release'
    success, amazon_facts = distro_files.parse_distribution_file_Amazon('Amazon', data, path, {})
    
    assert success is True
    assert amazon_facts['distribution'] == 'Amazon'
    assert amazon_facts['distribution_version'] == '1.0'
    assert amazon_facts['distribution_major_version'] == '1'
    assert amazon_facts['distribution_minor_version'] == '0'

def test_edge_case_empty_file(distro_files):
    data = ''
    path = '/etc/os-release'
    success, amazon_facts = distro_files.parse_distribution_file_Amazon('Amazon', data, path, {})
    
    assert success is False
    assert not amazon_facts

def test_invalid_input_missing_amazon_string(distro_files):
    data = 'This is not Amazon'
    path = '/etc/os-release'
    success, amazon_facts = distro_files.parse_distribution_file_Amazon('Amazon', data, path, {})
    
    assert success is False
    assert not amazon_facts
