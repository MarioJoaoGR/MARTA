
import pytest
from ansible.module_utils.facts.collector import _get_requires_by_collector_name, CollectorNotFoundError

# Test Case 1: Retrieving Required Facts for a Specific Collector (Existing)
def test_get_requires_by_collector_name_valid():
    class CPUCollector:
        required_facts = {'cpu_speed', 'cpu_cores'}

    class MemoryCollector:
        required_facts = {'memory_total', 'memory_used'}

    all_fact_subsets = {
        'cpu': [CPUCollector],
        'memory': [MemoryCollector]
    }
    
    required_facts = _get_requires_by_collector_name('memory', all_fact_subsets)
    assert required_facts == {'memory_total', 'memory_used'}

# Test Case 2: Handling Case Where Collector Is Not Found (Existing)
def test_get_requires_by_collector_name_not_found():
    class CPUCollector:
        required_facts = {'cpu_speed', 'cpu_cores'}

    all_fact_subsets = {
        'cpu': [CPUCollector]
    }
    
    with pytest.raises(CollectorNotFoundError) as excinfo:
        _get_requires_by_collector_name('memory', all_fact_subsets)