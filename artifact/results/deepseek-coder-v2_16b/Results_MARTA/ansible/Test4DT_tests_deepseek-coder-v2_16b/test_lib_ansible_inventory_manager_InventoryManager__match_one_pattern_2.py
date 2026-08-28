
import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import patch

# Test 1: test_valid_pattern_match
def test_valid_pattern_match():
    # Create a real instance of InventoryManager with sources=['hosts.yml']
    manager = InventoryManager(sources=['hosts.yml'])
    
    # Call the _match_one_pattern method with a valid pattern
    matched_hosts = manager._match_one_pattern('webserver')
    
    # Assert that the result is not empty and contains expected host names
    assert len(matched_hosts) > 0, "Expected hosts to match the pattern 'webserver'"
    assert isinstance(matched_hosts, list), "Expected a list of matched hosts"

# Test 2: test_missing_subscript_error
def test_missing_subscript_error():
    # Create an instance of InventoryManager with an invalid pattern and sources=['hosts.yml']
    manager = InventoryManager(sources=['hosts.yml'], pattern='webserver[99]')
    
    # Call the _match_one_pattern method which should raise IndexError
    with pytest.raises(IndexError):
        matched_hosts = manager._match_one_pattern('webserver[99]')

# Test 3: test_invalid_pattern_input
def test_invalid_pattern_input():
    # Create an instance of InventoryManager without any pattern or sources
    manager = InventoryManager()
    
    # Call the _match_one_pattern method with an invalid pattern
    with pytest.raises(TypeError):
        matched_hosts = manager._match_one_pattern('invalid_pattern')
