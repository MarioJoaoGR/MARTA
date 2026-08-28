
# Module: ansible.module_utils.facts.collector
from ansible.module_utils.facts.collector import BaseFactCollector
import pytest

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

def test_transform_dict_keys_empty():
    class CustomNamespace:
        def transform(self, name):
            return 'prefix_' + name
    
    namespace = CustomNamespace()
    fact_collector = BaseFactCollector(namespace=namespace)
    original_dict = {}
    transformed_dict = fact_collector._transform_dict_keys(original_dict.copy())
    assert len(transformed_dict) == 0

def test_transform_dict_keys_single_item():
    class CustomNamespace:
        def transform(self, name):
            return 'prefix_' + name
    
    namespace = CustomNamespace()
    fact_collector = BaseFactCollector(namespace=namespace)
    original_dict = {'old_key1': 'value1'}
    transformed_dict = fact_collector._transform_dict_keys(original_dict.copy())
    assert len(transformed_dict) == 1