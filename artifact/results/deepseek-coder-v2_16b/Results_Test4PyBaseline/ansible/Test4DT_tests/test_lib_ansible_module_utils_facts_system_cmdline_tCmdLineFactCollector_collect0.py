# Module: ansible.module_utils.facts.system.cmdline
import pytest
from lib.ansible.module_utils.facts.system.cmdline import CmdLineFactCollector

# Test fixture to create an instance of CmdLineFactCollector for each test
@pytest.fixture(scope="function")
def cmdline_collector():
    return CmdLineFactCollector()

# Test case to check if the collect method returns a dictionary when data is available
def test_collect_with_data(cmdline_collector):
    collected_facts = cmdline_collector.collect()
    assert isinstance(collected_facts, dict), "Expected a dictionary but got something else"
    assert 'cmdline' in collected_facts, "Expected 'cmdline' key to be present in the returned dictionary"
    assert 'proc_cmdline' in collected_facts, "Expected 'proc_cmdline' key to be present in the returned dictionary"

# Test case to check if the collect method returns an empty dictionary when data is not available
def test_collect_without_data(cmdline_collector):
    class MockCmdLineFactCollector:
        def _get_proc_cmdline(self):
            return None
    
    collector = MockCmdLineFactCollector()
    collected_facts = collector.collect()
    assert isinstance(collected_facts, dict), "Expected a dictionary but got something else"
    assert len(collected_facts) == 0, "Expected an empty dictionary when no data is available"

# Test case to check if the collect method processes command line arguments correctly
def test_collect_processes_data_correctly(cmdline_collector):
    class MockCmdLineFactCollector:
        def _get_proc_cmdline(self):
            return "key1=value1 key2=value2"
        
        def _parse_proc_cmdline(self, data):
            return {'key1': 'value1', 'key2': 'value2'}
        
        def _parse_proc_cmdline_facts(self, data):
            return {'parsed': True}
    
    collector = MockCmdLineFactCollector()
    collected_facts = collector.collect()
    assert isinstance(collected_facts, dict), "Expected a dictionary but got something else"
    assert collected_facts['cmdline'] == {'key1': 'value1', 'key2': 'value2'}, "Expected cmdline to be parsed correctly"
    assert collected_facts['proc_cmdline'] == {'parsed': True}, "Expected proc_cmdline to be processed correctly"
