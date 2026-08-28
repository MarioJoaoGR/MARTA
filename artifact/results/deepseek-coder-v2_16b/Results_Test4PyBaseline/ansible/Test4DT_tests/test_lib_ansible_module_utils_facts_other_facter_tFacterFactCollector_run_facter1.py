
import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.other.facter import FacterFactCollector

# Fixture to create a mock module for testing
@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path = lambda binary_name, opt_dirs=None: '/usr/local/bin/facter' if binary_name == 'facter' else None
    return module

# Test case for running facter with a module using the correct path and arguments
def test_run_facter_correct_path(mock_module):
    facter_collector = FacterFactCollector()
    mock_module.run_command.return_value = (0, 'output', '')  # Correcting the return value of run_command to match expected output
    rc, out, err = facter_collector.run_facter(mock_module, '/usr/local/bin/facter')
    mock_module.run_command.assert_called_with('/usr/local/bin/facter --puppet --json')
    assert rc == 0
    assert out == 'output'
    assert err == ''

# Test case for running facter with a module that fails to execute (non-zero return code)
def test_run_facter_failure(mock_module):
    mock_module.run_command.return_value = (1, '', 'Error executing facter')  # Correcting the return value of run_command to match expected output
    facter_collector = FacterFactCollector()
    rc, out, err = facter_collector.run_facter(mock_module, '/usr/local/bin/facter')
    mock_module.run_command.assert_called_with('/usr/local/bin/facter --puppet --json')
    assert rc == 1
    assert out == ''