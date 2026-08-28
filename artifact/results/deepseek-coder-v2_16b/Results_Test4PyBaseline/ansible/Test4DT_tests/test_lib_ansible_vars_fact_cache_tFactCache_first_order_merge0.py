# Module: ansible.vars.fact_cache
import pytest
from ansible.vars.fact_cache import FactCache
from ansible.errors import AnsibleError

# Test Case 1: Basic Initialization
def test_basic_initialization():
    fact_cache = FactCache()
    assert hasattr(fact_cache, '_plugin'), "FactCache instance should have a _plugin attribute"

# Test Case 2: Custom Cache Plugin Initialization
def test_custom_cache_plugin_initialization():
    with pytest.raises(AnsibleError):
        FactCache(plugin='non_existent_plugin')

# Test Case 3: Retrieving Non-Existent Facts
def test_retrieving_nonexistent_facts():
    fact_cache = FactCache()
    with pytest.raises(KeyError):
        value = fact_cache['nonexistent_key']

# Test Case 4: Setting New Facts
def test_setting_new_facts():
    fact_cache = FactCache()
    fact_cache['new_fact_key'] = "new_fact_value"
    assert 'new_fact_key' in fact_cache, "The key should be present in the cache after setting it"

# Test Case 5: Deleting Facts
def test_deleting_facts():
    fact_cache = FactCache()
    fact_cache['delete_test_key'] = "delete_test_value"
    del fact_cache['delete_test_key']
    with pytest.raises(KeyError):
        value = fact_cache['delete_test_key']

# Test Case 6: Checking for Key Membership
def test_checking_for_key_membership():
    fact_cache = FactCache()
    assert 'new_fact_key' not in fact_cache, "The key should not be present in the cache initially"
    fact_cache['new_fact_key'] = "new_fact_value"
    assert 'new_fact_key' in fact_cache, "The key should be present in the cache after setting it"

# Test Case 7: First-Order Merge of Facts
def test_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('network', {'ip': '192.168.1.1', 'netmask': '255.255.255.0'})
    assert 'network' in fact_cache, "The key should be present in the cache after merging facts"
    assert fact_cache['network'] == {'ip': '192.168.1.1', 'netmask': '255.255.255.0'}, "The merged facts should match the expected values"
