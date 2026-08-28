
import pytest
from ansible.module_utils.facts.ansible_collector import CollectorMetaDataCollector

# Example 1: Default Initialization with No Additional Parameters
def test_default_initialization():
    collector = CollectorMetaDataCollector()
    meta_facts = collector.collect()
    assert 'gather_subset' in meta_facts and meta_facts['gather_subset'] is None
    assert 'module_setup' not in meta_facts, f"Expected module_setup to be missing but got {meta_facts}"

# Example 2: Custom Namespace and Gather Subset
def test_custom_namespace_and_gather_subset():
    collector = CollectorMetaDataCollector(namespace='custom_namespace', gather_subset=['all'])
    meta_facts = collector.collect()
    assert 'gather_subset' in meta_facts and meta_facts['gather_subset'] == ['all']
    assert 'module_setup' not in meta_facts, f"Expected module_setup to be missing but got {meta_facts}"

# Example 3: Including Additional Setup Parameters
def test_including_additional_setup_parameters():
    collector = CollectorMetaDataCollector(namespace='example', gather_subset=['min'], module_setup={'option1': 'value1'})
    meta_facts = collector.collect()
    assert 'gather_subset' in meta_facts and meta_facts['gather_subset'] == ['min']
    assert 'module_setup' in meta_facts and meta_facts['module_setup'] == {'option1': 'value1'}

# Example 4: Using with Other Collectors
class OtherCollector:
    def collect(self):
        return {'example_fact': 'example_value'}

def test_using_with_other_collectors():
    collector = CollectorMetaDataCollector(collectors=[OtherCollector()], namespace='example', gather_subset=['all'], module_setup={'option1': 'value1'})
    meta_facts = collector.collect()