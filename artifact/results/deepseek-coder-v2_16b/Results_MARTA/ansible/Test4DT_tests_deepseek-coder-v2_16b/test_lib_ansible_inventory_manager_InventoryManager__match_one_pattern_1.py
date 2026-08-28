
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError

# Test case for valid pattern match

# Test case for invalid pattern match
def test_invalid_pattern_match():
    # Create a real instance of InventoryManager with sources=['hosts']
    manager = InventoryManager(loader=None, sources=['hosts'])
    
    # Test the _match_one_pattern method with an invalid pattern
    matched_hosts = manager._match_one_pattern('invalid_pattern')
    assert isinstance(matched_hosts, list), "Expected a list of hosts"
    assert 'invalid_pattern' not in matched_hosts, "Expected 'invalid_pattern' to be absent in the matched hosts list"