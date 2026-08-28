
import pytest
from ansible.module_utils.facts.collector import BaseFactCollector
from collections import namedtuple

# Define a simple namespace transformer for testing
class NamespaceTransformer:
    def transform(self, name):
        return f"ns_{name}"

# Define some fact collectors for testing
class CustomFactCollector:
    pass

class AnotherFactCollector:
    pass

BaseFact = namedtuple('BaseFact', ['id'])

def test_valid_input():
    namespace_obj = NamespaceTransformer()
    fact_collectors = [CustomFactCollector(), AnotherFactCollector()]
    base_fact_collector = BaseFactCollector(collectors=fact_collectors, namespace=namespace_obj)
    
    assert isinstance(base_fact_collector.collectors, list)
    assert len(base_fact_collector.collectors) == 2
    assert isinstance(base_fact_collector.namespace, NamespaceTransformer)
    assert set(base_fact_collector.fact_ids) == {'BaseFactCollector'}

def test_edge_case():
    base_fact_collector = BaseFactCollector(collectors=None, namespace=None)
    
    assert isinstance(base_fact_collector.collectors, list)
    assert len(base_fact_collector.collectors) == 0
    assert base_fact_collector.namespace is None
    assert set(base_fact_collector.fact_ids) == {'BaseFactCollector'}

def test_invalid_input():
    with pytest.raises(TypeError):
        base_fact_collector = BaseFactCollector(collectors=[], namespace='InvalidNamespace')
