
import pytest
from ansible.module_utils.facts.other.ohai import OhaiFactCollector

# Fixture to create an instance of OhaiFactCollector for testing
@pytest.fixture
def ohai_collector():
    return OhaiFactCollector(collectors={'cpu', 'memory'}, namespace='custom_ohai')

# Test case for initializing OhaiFactCollector with specific collectors and namespace
def test_init_with_specific_collectors_and_namespace(ohai_collector):
    assert str(ohai_collector.namespace) == "PrefixFactNamespace(namespace_name='custom_ohai', prefix='ohai_')"

# Test case for finding the path to the Ohai executable
def test_find_ohai(mocker):
    module = mocker.Mock()
    module.get_bin_path.return_value = '/usr/local/bin/ohai'
    ohai_collector = OhaiFactCollector(collectors={'cpu', 'memory'}, namespace='custom_ohai')
    assert ohai_collector.find_ohai(module) == '/usr/local/bin/ohai'

# Test case for running the Ohai command and capturing output, return code, and error
def test_run_ohai(mocker):
    module = mocker.Mock()
    ohai_path = '/usr/local/bin/ohai'
    mocker.patch('subprocess.run', return_value=mocker.Mock(returncode=0, stdout='output', stderr='error'))
    ohai_collector = OhaiFactCollector(collectors={'cpu', 'memory'}, namespace='custom_ohai')
    rc, out, err = ohai_collector.run_ohai(module, ohai_path)
    assert rc == 0
    assert out == 'output'
    assert err == 'error'

# Test case for collecting Ohai facts from a specified module
def test_collect_facts():
    class ModuleMock:
        def __init__(self):
            self.params = {'custom_ohai_cpu': 'value1', 'custom_ohai_memory': 'value2'}
    
    module = ModuleMock()
    ohai_collector = OhaiFactCollector(collectors={'cpu', 'memory'}, namespace='custom_ohai')
    facts = ohai_collector.collect(module=module)
    assert facts == {'cpu': 'value1', 'memory': 'value2'}
