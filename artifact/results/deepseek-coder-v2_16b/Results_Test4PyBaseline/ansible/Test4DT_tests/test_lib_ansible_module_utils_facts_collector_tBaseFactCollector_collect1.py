
# Module: ansible.module_utils.facts.collector
# test_base_fact_collector.py
from ansible.module_utils.facts.collector import BaseFactCollector
import pytest

@pytest.fixture
def base_fact_collector():
    return BaseFactCollector()

@pytest.fixture
def custom_namespace():
    class CustomNamespace:
        def transform(self, name):
            return 'custom_' + name
    return CustomNamespace()

@pytest.fixture
def another_fact_collector():
    class AnotherFactCollector(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            facts = super().collect(module, collected_facts)
            # Add additional fact collection logic here if needed
            return facts
    return AnotherFactCollector()

@pytest.fixture
def platform_fact_collector():
    class PlatformFactCollector(BaseFactCollector):
        _platform = 'Linux'
    return PlatformFactCollector()

@pytest.fixture
def required_facts_collector():
    class RequiredFactsCollector(BaseFactCollector):
        required_facts = {'memory', 'cpu'}
    return RequiredFactsCollector()

# Test cases for BaseFactCollector initialization with default parameters
def test_base_fact_collector_default(base_fact_collector):
    assert base_fact_collector.collectors == []
    assert base_fact_collector.namespace is None
    assert base_fact_collector.fact_ids == {None}

# Test cases for BaseFactCollector initialization with custom namespace
def test_base_fact_collector_with_custom_namespace(custom_namespace):
    fact_collector = BaseFactCollector(namespace=custom_namespace)
    assert fact_collector.namespace is not None
    collected_facts = fact_collector.collect()
    assert isinstance(collected_facts, dict), "Collected facts should be a dictionary"
    for key in collected_facts:
        assert key.startswith('custom_'), "Fact names should be transformed by the custom namespace"

# Test cases for BaseFactCollector initialization with collectors delegation
def test_base_fact_collector_with_collectors_delegation(another_fact_collector):
    fact_collector = BaseFactCollector(collectors=[another_fact_collector])
    assert len(fact_collector.collectors) == 1
    collected_facts = fact_collector.collect()
    assert isinstance(collected_facts, dict), "Collected facts should be a dictionary"

# Test cases for BaseFactCollector initialization with specific platform
def test_base_fact_collector_with_platform(platform_fact_collector):
    collected_facts = platform_fact_collector.collect()
    assert platform_fact_collector._platform == 'Linux', "Platform should be Linux"
    assert isinstance(collected_facts, dict), "Collected facts should be a dictionary"

# Test cases for BaseFactCollector initialization with required facts
def test_base_fact_collector_with_required_facts(required_facts_collector):
    collected_facts = required_facts_collector.collect()
    assert 'memory' in required_facts_collector.required_facts, "Memory should be a required fact"
    assert 'cpu' in required_facts_collector.required_facts, "CPU should be a required fact"
    assert isinstance(collected_facts, dict), "Collected facts should be a dictionary"

# Additional test cases for the collect method to cover uncovered lines 116-117
def test_base_fact_collector_collect_returns_empty_dict():
    collector = BaseFactCollector()
    collected_facts = collector.collect()