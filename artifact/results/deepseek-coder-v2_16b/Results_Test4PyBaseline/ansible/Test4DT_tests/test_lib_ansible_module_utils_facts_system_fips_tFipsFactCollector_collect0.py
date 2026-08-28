# Module: ansible.module_utils.facts.system.fips
import pytest
from ansible.module_utils.facts.system.fips import FipsFactCollector

# Assuming get_file_content is a function that reads from '/proc/sys/crypto/fips_enabled'
def get_file_content(path):
    with open(path, 'r') as file:
        return file.read().strip()

@pytest.fixture
def fips_collector():
    return FipsFactCollector()

# Test cases for the collect method
def test_fips_enabled(mocker, fips_collector):
    # Mock get_file_content to return '1' indicating FIPS is enabled
    mocker.patch('ansible.module_utils.facts.system.fips.get_file_content', return_value='1')
    result = fips_collector.collect()
    assert result == {'fips': True}

def test_fips_disabled(mocker, fips_collector):
    # Mock get_file_content to return None or any other value indicating FIPS is disabled
    mocker.patch('ansible.module_utils.facts.system.fips.get_file_content', return_value=None)
    result = fips_collector.collect()
    assert result == {'fips': False}

def test_no_such_file(mocker, fips_collector):
    # Mock get_file_content to raise a FileNotFoundError indicating the file does not exist
    mocker.patch('ansible.module_utils.facts.system.fips.get_file_content', side_effect=FileNotFoundError)
    result = fips_collector.collect()
    assert result == {'fips': False}

def test_empty_file(mocker, fips_collector):
    # Mock get_file_content to return an empty string indicating the file is empty
    mocker.patch('ansible.module_utils.facts.system.fips.get_file_content', return_value='')
    result = fips_collector.collect()
    assert result == {'fips': False}
