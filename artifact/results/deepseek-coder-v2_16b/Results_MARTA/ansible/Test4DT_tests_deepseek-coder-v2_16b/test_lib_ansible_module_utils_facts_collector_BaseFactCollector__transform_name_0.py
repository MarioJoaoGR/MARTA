
import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

# Test Scenario 1: Valid Case
def test_valid_case():
    class CustomFactCollector1(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {"custom_fact_1": "example"}
    
    class CustomFactCollector2(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {"custom_fact_2": "example"}
    
    class NamespaceTransformer:
        def transform(self, key_name):
            return f"namespace_{key_name}"
    
    namespace_obj = NamespaceTransformer()
    fact_collectors = [CustomFactCollector1(), CustomFactCollector2()]
    base_fact_collector = BaseFactCollector(collectors=fact_collectors, namespace=namespace_obj)
    
    assert isinstance(base_fact_collector.collectors, list)
    assert len(base_fact_collector.collectors) == 2
    assert all(isinstance(c, BaseFactCollector) for c in base_fact_collector.collectors)
    assert base_fact_collector.namespace is not None
    assert callable(getattr(base_fact_collector.namespace, 'transform', None))

# Test Scenario 2: Edge Case
def test_edge_case():
    base_fact_collector = BaseFactCollector(collectors=None, namespace=None)
    
    assert isinstance(base_fact_collector.collectors, list)
    assert len(base_fact_collector.collectors) == 0
    assert base_fact_collector.namespace is None

# Test Scenario 3: Error Case
def test_error_case():
    with pytest.raises(TypeError):
        BaseFactCollector(collectors='invalid', namespace='invalid')
