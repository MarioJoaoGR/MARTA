
# Module: ansible.module_utils.facts.collector
from ansible.module_utils.facts.collector import BaseFactCollector
import pytest

def test_collect_with_namespace_default():
    fact_collector = BaseFactCollector()
    collected_facts = {'example_fact': 'value'}
    transformed_facts = fact_collector.collect_with_namespace(collected_facts=collected_facts)
    assert transformed_facts == {}, "Expected an empty dictionary when no namespace is defined."

def test_collect_with_namespace_custom_namespace():
    class CustomNamespace:
        def transform(self, name):
            return 'prefix_' + name

    custom_namespace = CustomNamespace()
    fact_collector = BaseFactCollector(namespace=custom_namespace)
    
    collected_facts = {'example_fact': 'value'}
    transformed_facts = fact_collector.collect_with_namespace(collected_facts=collected_facts)