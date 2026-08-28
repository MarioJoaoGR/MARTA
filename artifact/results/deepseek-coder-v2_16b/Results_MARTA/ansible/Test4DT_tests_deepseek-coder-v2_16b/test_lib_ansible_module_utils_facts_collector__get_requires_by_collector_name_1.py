
import pytest
from ansible.module_utils.facts.collector import CollectorNotFoundError

# Scenario 1: Test standard input
def test_valid_case():
    class CPUCollector:
        required_facts = {'cpu_fact1', 'cpu_fact2'}
    
    class MemoryCollector:
        required_facts = {'memory_fact1', 'memory_fact2'}
    
    class DiskUsageCollector:
        required_facts = {'disk_fact1', 'disk_fact2'}
    
    all_fact_subsets = {
        'cpu': [CPUCollector, MemoryCollector],
        'disk': [DiskUsageCollector]
    }
    
    collector_name = 'cpu'
    required_facts = _get_requires_by_collector_name(collector_name, all_fact_subsets)
    
    assert len(required_facts) == 4
    assert 'cpu_fact1' in required_facts
    assert 'cpu_fact2' in required_facts
    assert 'memory_fact1' in required_facts
    assert 'memory_fact2' in required_facts

# Scenario 2: Test with None as collector name
def test_edge_case():
    all_fact_subsets = {}
    collector_name = None
    
    with pytest.raises(CollectorNotFoundError):
        _get_requires_by_collector_name(collector_name, all_fact_subsets)

# Scenario 3: Test raising CollectorNotFoundError
def test_error_case():
    all_fact_subsets = {}
    collector_name = 'unknown'
    
    with pytest.raises(CollectorNotFoundError):
        _get_requires_by_collector_name(collector_name, all_fact_subsets)
