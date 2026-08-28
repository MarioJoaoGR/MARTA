
import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

# Test initialization without collectors and namespace

# Test initialization with collectors and namespace

# Test transforming a key name with namespace
def test_base_fact_collector_transform_name():
    class NamespaceTransformer:
        def transform(self, key_name):
            return f"namespace_{key_name}"
    
    namespace_obj = NamespaceTransformer()
    collector = BaseFactCollector(namespace=namespace_obj)
    transformed_key_name = collector._transform_name("some_fact")
    assert transformed_key_name == "namespace_some_fact"