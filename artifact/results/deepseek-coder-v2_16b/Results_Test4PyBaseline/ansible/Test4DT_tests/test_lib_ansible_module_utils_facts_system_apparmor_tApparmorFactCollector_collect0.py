# Module: ansible.module_utils.facts.system.apparmor
import pytest
import os
from ansible.module_utils.facts.system.apparmor import ApparmorFactCollector

# Fixture to create an instance of the class for testing
@pytest.fixture
def collector():
    return ApparmorFactCollector()

# Test case to check if AppArmor is enabled when the file exists
def test_collect_enabled(collector, mocker):
    # Mocking os.path.exists to return True (AppArmor is enabled)
    mocker.patch('os.path.exists', return_value=True)
    
    result = collector.collect()
    assert 'apparmor' in result
    assert result['apparmor']['status'] == 'enabled'

# Test case to check if AppArmor is disabled when the file does not exist
def test_collect_disabled(collector, mocker):
    # Mocking os.path.exists to return False (AppArmor is disabled)
    mocker.patch('os.path.exists', return_value=False)
    
    result = collector.collect()
    assert 'apparmor' in result
    assert result['apparmor']['status'] == 'disabled'
