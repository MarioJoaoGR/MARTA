# Module: ansible.module_utils.facts.other.facter
import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.other.facter import FacterFactCollector

# Fixture to create a mock module for testing
@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path = lambda binary_name, opt_dirs=None: '/usr/local/bin/facter' if binary_name == 'facter' else None
    return module

# Test case for default initialization of FacterFactCollector
def test_default_initialization():
    facter_collector = FacterFactCollector()
    assert facter_collector.namespace.namespace_name == 'facter'
    assert facter_collector.namespace.prefix == 'facter_'
    assert set(facter_collector._fact_ids) == {'facter'}

# Test case for custom namespace and collectors initialization of FacterFactCollector
def test_custom_initialization():
    facter_collector = FacterFactCollector(collectors={'facter'}, namespace='custom_namespace')
    assert facter_collector.namespace.namespace_name == 'facter'
    assert facter_collector.namespace.prefix == 'facter_'
    assert set(facter_collector._fact_ids) == {'facter'}

# Test case for running facter with a module
def test_run_facter(mock_module):
    facter_collector = FacterFactCollector()
    rc, out, err = facter_collector.run_facter(mock_module, '/usr/local/bin/facter')
    mock_module.run_command.assert_called_with('/usr/local/bin/facter --puppet --json')
    assert rc == 0
    assert out == ''
    assert err == ''

# Test case for running facter with a module that fails to execute (non-zero return code)
def test_run_facter_failure(mock_module):
    mock_module.run_command.return_value = (1, '', 'Error executing facter')
    facter_collector = FacterFactCollector()
    rc, out, err = facter_collector.run_facter(mock_module, '/usr/local/bin/facter')
    mock_module.run_command.assert_called_with('/usr/local/bin/facter --puppet --json')
    assert rc == 1
    assert out == ''
    assert err == 'Error executing facter'
