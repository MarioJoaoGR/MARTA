# Module: ansible.module_utils.facts.system.distribution
import pytest
from ansible.module_utils.facts.system.distribution import DistributionFactCollector

# Create an instance of the collector
@pytest.fixture
def collector():
    return DistributionFactCollector()

def test_collect_with_valid_module(collector):
    # Mock module with system information
    class MockModule:
        def get_facts(self):
            return {'os': 'Linux', 'distribution': 'Ubuntu', 'version': '18.04'}
    
    module = MockModule()
    collected_info = collector.collect(module=module)
    assert isinstance(collected_info, dict), "Expected a dictionary but got something else."
    assert 'os' in collected_info, "Expected 'os' key to be present in the returned dictionary."
    assert collected_info['os'] == 'Linux', f"Expected os to be Linux, but got {collected_info['os']}."
    assert 'distribution' in collected_info, "Expected 'distribution' key to be present in the returned dictionary."
    assert collected_info['distribution'] == 'Ubuntu', f"Expected distribution to be Ubuntu, but got {collected_info['distribution']}."
    assert 'version' in collected_info, "Expected 'version' key to be present in the returned dictionary."
    assert collected_info['version'] == '18.04', f"Expected version to be 18.04, but got {collected_info['version']}."

def test_collect_without_module(collector):
    collected_info = collector.collect()
    assert collected_info == {}, "Expected an empty dictionary when no module is provided."

def test_collect_with_invalid_module(collector):
    # Mock an invalid module
    class InvalidMockModule:
        pass
    
    module = InvalidMockModule()
    collected_info = collector.collect(module=module)
    assert collected_info == {}, "Expected an empty dictionary when providing an invalid module."
