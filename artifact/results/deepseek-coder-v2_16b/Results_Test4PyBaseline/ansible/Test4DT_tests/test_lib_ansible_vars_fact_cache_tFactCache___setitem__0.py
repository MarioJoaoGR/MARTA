# Module: ansible.vars.fact_cache
import pytest
from your_module import FactCache
from ansible.errors import AnsibleError

# Fixture to create a FactCache instance for testing
@pytest.fixture
def fact_cache():
    return FactCache()

# Test case for initializing a FactCache instance without any parameters
def test_fact_cache_init():
    with pytest.raises(AnsibleError):
        FactCache()

# Test case for setting and retrieving a value from the cache
def test_set_and_get_item(fact_cache):
    fact_cache['test_key'] = 'test_value'
    assert fact_cache['test_key'] == 'test_value'

# Test case for checking if a key exists in the cache
def test_contains_key(fact_cache):
    with pytest.raises(KeyError):
        fact_cache['non_existent_key']  # This should raise KeyError because the key does not exist

# Test case for setting a new value for a key
def test_set_item(fact_cache):
    fact_cache['new_key'] = 'new_value'
    assert fact_cache['new_key'] == 'new_value'

# Test case for deleting a key from the cache
def test_delete_item(fact_cache):
    fact_cache['to_be_deleted'] = 'value_to_be_deleted'
    del fact_cache['to_be_deleted']
    with pytest.raises(KeyError):
        fact_cache['to_be_deleted']  # This should raise KeyError because the key has been deleted

# Test case for checking if a key exists in the cache after deletion
def test_key_not_in_cache_after_deletion(fact_cache):
    fact_cache['check_key'] = 'value'
    del fact_cache['check_key']
    with pytest.raises(KeyError):
        fact_cache['check_key']  # This should raise KeyError because the key has been deleted
