
# Module: ansible.module_utils.facts.collector
# test_base_fact_collector.py
from ansible.module_utils.facts.collector import BaseFactCollector
import pytest

def test_transform_dict_keys():
    class CustomNamespace:
        def transform(self, name):
            return 'prefix_' + name
    
    namespace = CustomNamespace()
    fact_collector = BaseFactCollector(namespace=namespace)
    
    # Test with a simple dictionary
    original_dict = {'old_key1': 'value1', 'old_key2': 'value2'}
    transformed_dict = fact_collector._transform_dict_keys(original_dict.copy())
    assert len(transformed_dict) == 2, "Expected two keys in the transformed dictionary"
    assert transformed_dict['prefix_old_key1'] == 'value1', "The key should be prefixed with 'prefix_'"
    assert transformed_dict['prefix_old_key2'] == 'value2', "The key should be prefixed with 'prefix_'"

def test_transform_dict_keys_empty():
    class CustomNamespace:
        def transform(self, name):
            return 'prefix_' + name
    
    namespace = CustomNamespace()
    fact_collector = BaseFactCollector(namespace=namespace)
    
    # Test with an empty dictionary
    original_dict = {}
    transformed_dict = fact_collector._transform_dict_keys(original_dict.copy())