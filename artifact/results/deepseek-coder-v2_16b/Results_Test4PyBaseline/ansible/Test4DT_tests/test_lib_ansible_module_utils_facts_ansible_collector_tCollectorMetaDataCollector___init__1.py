
# Module: ansible.module_utils.facts.ansible_collector
import pytest
from ansible.module_utils.facts.ansible_collector import CollectorMetaDataCollector

# Test default initialization of CollectorMetaDataCollector
def test_default_initialization():
    collector = CollectorMetaDataCollector()
    assert collector.namespace is None
    assert collector.gather_subset is None
    assert collector.module_setup is None

# Test initialization with namespace and gather subset
def test_with_namespace_and_gather_subset():
    collector = CollectorMetaDataCollector(namespace='example', gather_subset=['all'])
    assert collector.namespace == 'example'
    assert collector.gather_subset == ['all']
    assert collector.module_setup is None

# Test initialization with additional module setup parameters
def test_with_additional_module_setup():
    collector = CollectorMetaDataCollector(namespace='example', gather_subset=['min'], module_setup={'option1': 'value1'})
    assert collector.namespace == 'example'
    assert collector.gather_subset == ['min']
    assert collector.module_setup == {'option1': 'value1'}

# Test initialization with collectors
class OtherCollector:
    def collect(self):
        return {'example_fact': 'example_value'}

def test_with_collectors():
    collector = CollectorMetaDataCollector(collectors=[OtherCollector()], namespace='example', gather_subset=['all'], module_setup={'option1': 'value1'})
    assert isinstance(collector.collectors[0], OtherCollector)
    assert collector.namespace == 'example'
    assert collector.gather_subset == ['all']
    assert collector.module_setup == {'option1': 'value1'}

# Test initialization with only collectors
def test_only_with_collectors():
    class AnotherCollector:
        def collect(self):
            return {'another_fact': 'another_value'}
    
    collector = CollectorMetaDataCollector(collectors=[AnotherCollector()])
    assert isinstance(collector.collectors[0], AnotherCollector)
    assert collector.namespace is None
    assert collector.gather_subset is None
    assert collector.module_setup is None

# Test initialization with only namespace
def test_only_with_namespace():
    collector = CollectorMetaDataCollector(namespace='example')
    assert collector.namespace == 'example'
    assert collector.gather_subset is None
    assert collector.module_setup is None

# Test initialization with only module setup parameters
def test_only_with_module_setup():
    collector = CollectorMetaDataCollector(module_setup={'option1': 'value1'})
    assert collector.namespace is None
    assert collector.gather_subset is None
    assert collector.module_setup == {'option1': 'value1'}
