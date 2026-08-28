
import pytest
from ansible.plugins.inventory import ini

def test_InventoryModule_initialization():
    inv_module = ini.InventoryModule()
    assert isinstance(inv_module, ini.InventoryModule), "Initialization failed"

def test_parse_value_with_valid_int():
    value = '42'
    parsed_value = ini.InventoryModule._parse_value(value)
    assert parsed_value == 42, f"Expected int 42 but got {parsed_value}"

def test_parse_value_with_valid_dict():
    value = '{"key": "value"}'
    parsed_value = ini.InventoryModule._parse_value(value)
    assert parsed_value == {'key': 'value'}, f"Expected dict {{'key': 'value'}} but got {parsed_value}"

def test_parse_value_with_valid_list():
    value = '["item1", "item2"]'
    parsed_value = ini.InventoryModule._parse_value(value)
    assert parsed_value == ['item1', 'item2'], f"Expected list ['item1', 'item2'] but got {parsed_value}"

def test_parse_value_with_string():
    value = '"some text"'
    parsed_value = ini.InventoryModule._parse_value(value)
    assert parsed_value == "some text", f"Expected string 'some text' but got {parsed_value}"
