
import pytest
from ansible.vars.fact_cache import FactCache
from ansible.errors import AnsibleError

# Test initialization without parameters
def test_init_without_parameters():
    fact_cache = FactCache()
    assert hasattr(fact_cache, '_plugin'), "FactCache instance should have a _plugin attribute"

# Test flushing the cache
def test_flush_cache():
    fact_cache = FactCache()
    # Assuming there are some keys already in the cache for testing purposes
    fact_cache['key1'] = 'value1'
    fact_cache['key2'] = 'value2'
    
    # Before flushing, check that both keys exist
    assert 'key1' in fact_cache, "Key 'key1' should be in the cache before flush"
    assert 'key2' in fact_cache, "Key 'key2' should be in the cache before flush"
    
    # Flush the cache and check if keys are removed
    fact_cache.flush()
    with pytest.raises(KeyError):
        value = fact_cache['key1']  # This should raise a KeyError since the key was flushed
    with pytest.raises(KeyError):
        value = fact_cache['key2']  # This should raise a KeyError since the key was flushed

# Test flushing an empty cache
def test_flush_empty_cache():
    fact_cache = FactCache()
    
    # Before flushing, check that there are no keys in the cache
    with pytest.raises(KeyError):
        value = fact_cache['non_existent_key']  # This should raise a KeyError since the key does not exist
    
    # Flush the empty cache and ensure it doesn't raise an error
    fact_cache.flush()

# Test flushing after setting new facts
def test_flush_after_setting_facts():
    fact_cache = FactCache()
    
    # Set some initial keys
    fact_cache['key1'] = 'value1'
    fact_cache['key2'] = 'value2'
    
    # Before flushing, check that both keys exist
    assert 'key1' in fact_cache, "Key 'key1' should be in the cache before flush"
    assert 'key2' in fact_cache, "Key 'key2' should be in the cache before flush"
    
    # Flush the cache and check if keys are removed
    fact_cache.flush()
    with pytest.raises(KeyError):
        value = fact_cache['key1']  # This should raise a KeyError since the key was flushed
    with pytest.raises(KeyError):
        value = fact_cache['key2']  # This should raise a KeyError since the key was flushed
    
    # Add new keys after flushing and check if they exist
    fact_cache['new_key1'] = 'new_value1'
    fact_cache['new_key2'] = 'new_value2'
    assert 'new_key1' in fact_cache, "New key 'new_key1' should be in the cache after flush"
    assert 'new_key2' in fact_cache, "New key 'new_key2' should be in the cache after flush"
