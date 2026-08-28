# Module: ansible.module_utils.facts.other.facter
import pytest
from facter_fact_collector import FacterFactCollector

# Test default initialization of FacterFactCollector
def test_default_initialization():
    facter_collector = FacterFactCollector()
    assert facter_collector.namespace.prefix == 'facter_'
    assert set(facter_collector.collectors) == {'facter'}

# Test custom namespace and collectors initialization of FacterFactCollector
def test_custom_initialization():
    facter_collector = FacterFactCollector(collectors={'facter'}, namespace='custom_namespace')
    assert facter_collector.namespace.prefix == 'custom_namespace_'
    assert set(facter_collector.collectors) == {'facter'}

# Test finding the path to 'cfacter' if available, otherwise default to 'facter'
class MockModule:
    def get_bin_path(self, binary_name, opt_dirs=None):
        if binary_name == 'facter':
            return '/usr/local/bin/facter'
        elif binary_name == 'cfacter':
            return '/opt/puppetlabs/bin/cfacter'

@pytest.fixture
def mock_module():
    return MockModule()

# Test find_facter method with cfacter available
def test_find_facter_with_cfacter(mock_module):
    facter_collector = FacterFactCollector()
    path = facter_collector.find_facter(mock_module)
    assert path == '/opt/puppetlabs/bin/cfacter'

# Test find_facter method without cfacter available
def test_find_facter_without_cfacter(mock_module):
    mock_module.get_bin_path = lambda binary_name, opt_dirs=None: None
    facter_collector = FacterFactCollector()
    path = facter_collector.find_facter(mock_module)
    assert path == '/usr/local/bin/facter'

# Test collecting facts with 'facter' binary
class MockModuleRunCommand:
    def run_command(self, command):
        if command == '/usr/local/bin/facter --puppet --json':
            return (0, '{"os": "Linux", "memory": {"total": "8GB"}}', '')

@pytest.fixture
def mock_module_run_command():
    return MockModuleRunCommand()

def test_collect_facts_with_facter(mock_module_run_command):
    facter_collector = FacterFactCollector()
    module = mock_module_run_command
    collected_facts = facter_collector.collect(module=module)
    assert collected_facts == {'os': 'Linux', 'memory': {'total': '8GB'}}

# Test collecting facts with 'cfacter' binary
class MockModuleRunCommandCfacter:
    def run_command(self, command):
        if command == '/opt/puppetlabs/bin/cfacter --puppet --json':
            return (0, '{"os": "Linux", "memory": {"total": "16GB"}}', '')

@pytest.fixture
def mock_module_run_command_cfacter():
    return MockModuleRunCommandCfacter()

def test_collect_facts_with_cfacter(mock_module_run_command_cfacter):
    facter_collector = FacterFactCollector()
    module = mock_module_run_command_cfacter
    collected_facts = facter_collector.collect(module=module)
    assert collected_facts == {'os': 'Linux', 'memory': {'total': '16GB'}}
