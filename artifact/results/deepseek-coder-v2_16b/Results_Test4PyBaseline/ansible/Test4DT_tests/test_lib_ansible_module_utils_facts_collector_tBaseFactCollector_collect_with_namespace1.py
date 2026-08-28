
# Module: ansible.module_utils.facts.collector
from ansible.module_utils.facts.collector import BaseFactCollector
import pytest

def test_collect_with_namespace_no_module():
    fact_collector = BaseFactCollector()
    collected_facts = {}  # No facts provided
    result = fact_collector.collect_with_namespace(module=None, collected_facts=collected_facts)
    assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"
    assert len(result) == 0, f"Expected an empty dictionary but got {result}"

def test_collect_with_namespace_with_namespace():
    class CustomNamespace(object):
        def transform(self, name):
            return 'prefix_' + name

    custom_namespace = CustomNamespace()
    fact_collector = BaseFactCollector(namespace=custom_namespace)
    
    collected_facts = {'example_fact': 'value'}
    result = fact_collector.collect_with_namespace(module='test_module', collected_facts=collected_facts)
    assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"