# Module: ansible.module_utils.facts.collector
# test_base_fact_collector.py
from ansible.module_utils.facts.collector import BaseFactCollector

def test_init_without_parameters():
    collector = BaseFactCollector()
    assert collector.collectors == []
    assert collector.namespace is None
    assert collector.fact_ids == {None}

def test_init_with_collectors_and_namespace():
    class CustomNamespace:
        def transform(self, name):
            return 'prefix_' + name
    
    namespace = CustomNamespace()
    collectors = [BaseFactCollector()]
    collector = BaseFactCollector(collectors=collectors, namespace=namespace)
    assert isinstance(collector.collectors[0], BaseFactCollector)
    assert collector.namespace is not None
    assert collector.fact_ids == {None}

def test_transform_dict_keys():
    class CustomNamespace:
        def transform(self, name):
            return 'prefix_' + name
    
    namespace = CustomNamespace()
    fact_collector = BaseFactCollector(namespace=namespace)
    original_dict = {'old_key1': 'value1', 'old_key2': 'value2'}
    transformed_dict = fact_collector._transform_dict_keys(original_dict.copy())
    assert len(transformed_dict) == 2
    assert transformed_dict['prefix_old_key1'] == 'value1'
    assert transformed_dict['prefix_old_key2'] == 'value2'
