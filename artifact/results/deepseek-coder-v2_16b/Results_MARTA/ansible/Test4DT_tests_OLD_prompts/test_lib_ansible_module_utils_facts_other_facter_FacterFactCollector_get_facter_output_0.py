
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.other.facter import FacterFactCollector

# Test initialization with custom namespace

# Test get_facter_output method
def test_get_facter_output():
    module_mock = MagicMock()
    module_mock.return_value = {'path': '/usr/bin/facter'}
    
    with patch('ansible.module_utils.facts.other.facter.FacterFactCollector.find_facter', return_value='/usr/bin/facter'):
        facter_collector = FacterFactCollector()
        with patch('ansible.module_utils.facts.other.facter.FacterFactCollector.run_facter', return_value=(0, '{"os": "Linux"}', '')):
            output = facter_collector.get_facter_output(module_mock)
            assert output == '{"os": "Linux"}'

# Test get_facter_output method with non-zero return code
def test_get_facter_output_non_zero_return_code():
    module_mock = MagicMock()
    module_mock.return_value = {'path': '/usr/bin/facter'}
    
    with patch('ansible.module_utils.facts.other.facter.FacterFactCollector.find_facter', return_value='/usr/bin/facter'):
        facter_collector = FacterFactCollector()
        with patch('ansible.module_utils.facts.other.facter.FacterFactCollector.run_facter', return_value=(1, '', 'Error')):
            output = facter_collector.get_facter_output(module_mock)
            assert output is None