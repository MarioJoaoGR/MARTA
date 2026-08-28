
import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles


def test_parse_distribution_file_Amazon():
    # Create an instance and parse a valid Amazon distribution file
    distro_files = DistributionFiles(module='test')
    data = """NAME="Amazon Linux"
VERSION="2"
ID=amazon
VERSION_ID="2"
"""
    success, amazon_facts = distro_files.parse_distribution_file_Amazon('Amazon', data, '/etc/os-release', {})
    assert success is True
    assert amazon_facts['distribution'] == 'Amazon'
    assert amazon_facts['distribution_version'] == '2'
    assert amazon_facts['distribution_major_version'] == '2'
    assert amazon_facts['distribution_minor_version'] == 'NA'

def test_parse_distribution_file_Amazon_empty():
    # Create an instance and parse an empty Amazon distribution file
    distro_files = DistributionFiles(module='test')
    data = ""
    success, amazon_facts = distro_files.parse_distribution_file_Amazon('Amazon', data, '/etc/os-release', {})
    assert success is False
    assert not amazon_facts