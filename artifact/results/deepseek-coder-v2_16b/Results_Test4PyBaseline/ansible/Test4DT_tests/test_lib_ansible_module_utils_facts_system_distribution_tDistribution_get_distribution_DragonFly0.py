
# Module: ansible.module_utils.facts.system.distribution
# test_distribution.py
from ansible.module_utils.basic import AnsibleModule
import re
import platform
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture(scope="module")
def module():
    # Create a mock module object for testing
    return AnsibleModule(argument_spec={})

@pytest.fixture(scope="module")
def distribution(module):
    # Create an instance of the Distribution class for testing
    from ansible.module_utils.facts.system.distribution import Distribution  # Importing here to fix pylint error
    return Distribution(module)

class TestDistribution:
    
    def test_get_distribution_DragonFly_with_valid_output(self, distribution, module):
        with patch('ansible.module_utils.basic.AnsibleModule.run_command', return_value=(0, 'v13.0.0-RELEASE', None)):
            result = distribution.get_distribution_DragonFly()
            assert result == {'distribution_release': platform.release(), 'distribution_major_version': '13', 'distribution_version': '13.0.0'}
    
    def test_get_distribution_DragonFly_with_invalid_output(self, distribution, module):
        with patch('ansible.module_utils.basic.AnsibleModule.run_command', return_value=(0, 'unknown output', None)):
            result = distribution.get_distribution_DragonFly()
            assert result == {'distribution_release': platform.release()}
    
    def test_get_distribution_DragonFly_with_nonzero_return_code(self, distribution, module):
        with patch('ansible.module_utils.basic.AnsibleModule.run_command', return_value=(1, '', None)):
            result = distribution.get_distribution_DragonFly()
            assert result == {'distribution_release': platform.release()}
    
    def test_get_distribution_DragonFly_with_no_match(self, distribution, module):
        with patch('ansible.module_utils.basic.AnsibleModule.run_command', return_value=(0, 'v13.0.0-unknown', None)):
            result = distribution.get_distribution_DragonFly()
            assert result == {'distribution_release': platform.release()}
    
    def test_get_distribution_DragonFly_with_empty_output(self, distribution, module):
        with patch('ansible.module_utils.basic.AnsibleModule.run_command', return_value=(0, '', None)):
            result = distribution.get_distribution_DragonFly()
            assert result == {'distribution_release': platform.release()}
