
# Module: ansible.module_utils.facts.collector
# test_base_fact_collector.py
from ansible.module_utils.facts.collector import BaseFactCollector

def test_default_initialization():
    fact_collector = BaseFactCollector()
    assert fact_collector.collectors == []
    assert fact_collector.namespace is None
    assert fact_collector.fact_ids == {None}

def test_initialization_with_collectors_and_namespace():
    class CustomNamespace(object):
        def transform(self, name):
            return 'prefix_' + name

    class AnotherFactCollector(BaseFactCollector):
        pass

    custom_namespace = CustomNamespace()
    another_fact_collector = AnotherFactCollector()
    fact_collector = BaseFactCollector(collectors=[another_fact_collector], namespace=custom_namespace)
    
    assert isinstance(fact_collector.collectors, list)
    assert len(fact_collector.collectors) == 1
    assert isinstance(fact_collector.collectors[0], AnotherFactCollector)
    assert fact_collector.namespace is not None
    assert callable(fact_collector.namespace.transform)
    assert fact_collector.fact_ids == {None}

def test_collect():
    fact_collector = BaseFactCollector()
    collected_facts = fact_collector.collect()
    assert isinstance(collected_facts, dict)
    assert len(collected_facts) == 0

def test_collect_with_namespace():
    class CustomNamespace(object):
        def transform(self, name):
            return 'prefix_' + name

    custom_namespace = CustomNamespace()
    fact_collector = BaseFactCollector(namespace=custom_namespace)
    
    collected_facts = {'example_fact': 'value'}
    transformed_facts = fact_collector.collect_with_namespace(collected_facts=collected_facts)
    assert isinstance(transformed_facts, dict)