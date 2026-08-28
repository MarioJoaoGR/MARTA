
import pytest
from ansible.vars.fact_cache import FactCache
from ansible.errors import AnsibleError

# Test Case 8: Basic Initialization with Plugin
def test_basic_initialization_with_plugin():
    fact_cache = FactCache()
    assert hasattr(fact_cache, '_plugin'), "FactCache instance should have a _plugin attribute"

# Test Case 9: Retrieving Non-Existent Facts with Exception Handling
def test_retrieving_nonexistent_facts_with_exception():
    fact_cache = FactCache()
    with pytest.raises(KeyError):
        value = fact_cache['nonexistent_key']

# Test Case 10: Setting New Facts and Checking Membership
def test_setting_new_facts_and_membership():
    fact_cache = FactCache()
    fact_cache['new_fact_key'] = "new_fact_value"
    assert 'new_fact_key' in fact_cache, "The key should be present in the cache after setting it"
    assert fact_cache['new_fact_key'] == "new_fact_value", "The value of the new fact should match the set value"

# Test Case 11: Deleting Facts and Checking Non-Membership
def test_deleting_facts_and_non_membership():
    fact_cache = FactCache()
    fact_cache['delete_test_key'] = "delete_test_value"
    del fact_cache['delete_test_key']
    with pytest.raises(KeyError):
        value = fact_cache['delete_test_key']
    assert 'delete_test_key' not in fact_cache, "The key should not be present in the cache after deletion"

# Test Case 12: First-Order Merge of Facts with Existing Key
def test_first_order_merge_existing_key():
    fact_cache = FactCache()
    fact_cache['network'] = {'ip': '192.168.1.1', 'netmask': '255.255.255.0'}
    fact_cache.first_order_merge('network', {'gateway': '192.168.1.254'})
    assert 'network' in fact_cache, "The key should be present in the cache after merging facts"
    expected = {'ip': '192.168.1.1', 'netmask': '255.255.255.0', 'gateway': '192.168.1.254'}
    assert fact_cache['network'] == expected, "The merged facts should match the expected values"

# Test Case 13: First-Order Merge of Facts with Non-Existent Key
def test_first_order_merge_nonexistent_key():
    fact_cache = FactCache()
    fact_cache.first_order_merge('new_network', {'ip': '192.168.1.1', 'netmask': '255.255.255.0'})
    assert 'new_network' in fact_cache, "The key should be present in the cache after merging facts"
    expected = {'ip': '192.168.1.1', 'netmask': '255.255.255.0'}