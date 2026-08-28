
import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

# Test initialization of BaseFactCollector without collectors and namespace
def test_base_fact_collector_init():
    collector = BaseFactCollector()
    assert isinstance(collector, BaseFactCollector)
    assert collector.collectors == []
    assert collector.namespace is None
    assert collector.fact_ids == {None}

# Test initialization of BaseFactCollector with collectors
def test_base_fact_collector_init_with_collectors():
    class MockCollector(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {}
    
    collector1 = MockCollector()
    collector2 = MockCollector()
    collectors = [collector1, collector2]
    base_fact_collector = BaseFactCollector(collectors=collectors)
    assert isinstance(base_fact_collector, BaseFactCollector)
    assert len(base_fact_collector.collectors) == 2
    assert all(isinstance(c, BaseFactCollector) for c in base_fact_collector.collectors)

# Test initialization of BaseFactCollector with namespace
def test_base_fact_collector_init_with_namespace():
    class NamespaceTransformer:
        def transform(self, name):
            return f"ns_{name}"
    
    namespace_obj = NamespaceTransformer()
    base_fact_collector = BaseFactCollector(namespace=namespace_obj)
    assert isinstance(base_fact_collector, BaseFactCollector)
    assert base_fact_collector.namespace is not None
    assert base_fact_collector.namespace.transform("test") == "ns_test"

# Test collect method of BaseFactCollector
def test_base_fact_collector_collect():
    collector = BaseFactCollector()
    collected_facts = {}
    facts = collector.collect(collected_facts=collected_facts)
    assert isinstance(facts, dict)
    assert len(facts) == 0
