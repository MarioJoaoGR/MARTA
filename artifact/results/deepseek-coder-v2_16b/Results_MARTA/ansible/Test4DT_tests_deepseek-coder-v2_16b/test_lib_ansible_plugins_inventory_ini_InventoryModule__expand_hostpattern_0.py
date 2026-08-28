
import pytest
from unittest.mock import patch
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleParserError

# Test valid host pattern without port
def test_valid_hostpattern():
    inventory = InventoryModule()
    with patch('ansible.plugins.inventory.ini.InventoryModule._expand_hostpattern', return_value=(['hostname'], None)):
        result = inventory._expand_hostpattern("hostname")
        assert result == (['hostname'], None)

# Test valid host pattern with port
def test_valid_hostpattern_with_port():
    inventory = InventoryModule()
    with patch('ansible.plugins.inventory.ini.InventoryModule._expand_hostpattern', return_value=(['hostname'], 22)):
        result = inventory._expand_hostpattern("hostname:22")
        assert result == (['hostname'], 22)

# Test invalid host pattern ending with colon
def test_invalid_hostpattern_ending_with_colon():
    inventory = InventoryModule()
    with pytest.raises(AnsibleParserError):
        inventory._expand_hostpattern("hostname:")

# Test invalid host pattern containing '---'