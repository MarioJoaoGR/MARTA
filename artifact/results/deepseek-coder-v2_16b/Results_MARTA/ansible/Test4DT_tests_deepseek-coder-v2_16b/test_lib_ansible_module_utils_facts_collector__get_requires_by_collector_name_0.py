
import pytest
from ansible.module_utils.facts.collector import CollectorNotFoundError

# Assuming the following classes and their methods are defined in the module 'ansible.module_utils.facts.collector'
class CPUCollector:
    required_facts = {'cpu_fact1', 'cpu_fact2'}

class MemoryCollector:
    required_facts = {'memory_fact1', 'memory_fact2'}

class DiskUsageCollector:
    required_facts = {'disk_fact1', 'disk_fact2'}

def _get_requires_by_collector_name(collector_name, all_fact_subsets):
    """
    Retrieves the set of required facts for a specified fact collector.

    This function is designed to help users determine which facts are necessary for a specific fact collector by searching through a provided dictionary of fact collectors and their associated classes. It allows for efficient querying of required facts based on the name of the collector, making it easier to manage and understand dependencies between different data gathering components in a system.

    Parameters:
        collector_name (str): The name of the fact collector to query for its required facts.
        all_fact_subsets (dict): A dictionary containing various fact collectors, where keys are collector names and values are lists of classes representing these collectors.

    Returns:
        set: A set containing all the required facts for the specified fact collector.

    Raises:
        CollectorNotFoundError: If the specified fact collector is not found in `all_fact_subsets`.
    """
    required_facts = set()

    try:
        collector_classes = all_fact_subsets[collector_name]
    except KeyError:
        raise CollectorNotFoundError('Fact collector "%s" not found' % collector_name)
    for collector_class in collector_classes:
        required_facts.update(collector_class.required_facts)
    return required_facts

# Test cases
def test_valid_case_basic():
    all_fact_subsets = {
        'cpu': [CPUCollector, MemoryCollector],
        'disk': [DiskUsageCollector]
    }
    required_facts = _get_requires_by_collector_name('cpu', all_fact_subsets)
    assert required_facts == {'cpu_fact1', 'cpu_fact2', 'memory_fact1', 'memory_fact2'}

def test_error_case_missing_collector():
    all_fact_subsets = {
        'memory': [MemoryCollector],
        'disk': [DiskUsageCollector]
    }
    with pytest.raises(CollectorNotFoundError):
        _get_requires_by_collector_name('cpu', all_fact_subsets)

def test_error_case_invalid_input():
    all_fact_subsets = None
    with pytest.raises(TypeError):
        _get_requires_by_collector_name('cpu', all_fact_subsets)
