
import pytest
from ansible.module_utils.facts.collector import CPUCollector, MemoryCollector, DiskUsageCollector

def find_unresolved_requires(collector_names, all_fact_subsets):
    '''Find any collector names that have unresolved requires

    Returns a list of collector names that correspond to collector
    classes whose .requires_facts() are not in collector_names.
    '''
    unresolved = set()

    for collector_name in collector_names:
        required_facts = _get_requires_by_collector_name(collector_name, all_fact_subsets)
        for required_fact in required_facts:
            if required_fact not in collector_names:
                unresolved.add(required_fact)

    return unresolved

def test_valid_case():
    collector_names = ['cpu', 'memory']
    all_fact_subsets = {
        'cpu': [CPUCollector, MemoryCollector],
        'disk': [DiskUsageCollector]
    }
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert set(['cpu', 'memory']) == unresolved

def test_edge_case():
    collector_names = None
    all_fact_subsets = {
        'cpu': [CPUCollector, MemoryCollector],
        'disk': [DiskUsageCollector]
    }
    with pytest.raises(TypeError):
        find_unresolved_requires(collector_names, all_fact_subsets)

def test_error_case():
    collector_names = []
    all_fact_subsets = {}
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert set() == unresolved
