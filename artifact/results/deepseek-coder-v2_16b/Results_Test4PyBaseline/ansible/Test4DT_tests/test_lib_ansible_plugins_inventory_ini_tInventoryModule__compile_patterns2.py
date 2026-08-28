
import pytest
from ansible.plugins.inventory.ini import InventoryModule
import re
from textwrap import dedent

# Fixture to create an instance of InventoryModule for testing
@pytest.fixture
def inventory_module():
    inv = InventoryModule()
    return inv

# Test the initialization of InventoryModule
def test_inventory_module_initialization(inventory_module):
    assert hasattr(inventory_module, 'patterns')
    assert isinstance(inventory_module.patterns, dict)

# Test that the section pattern is compiled correctly
@pytest.mark.parametrize("input_text, expected", [
    ("[groupname]", True),
    ("[somegroup:vars]", True),
    ("[naughty:children]", True),
    ("[groupname:]", False),  # Invalid section name
    (" groupname]", False),   # Missing opening bracket
    ("[groupname] comment", False),  # Comment at the end of line
])
def test_section_pattern(inventory_module, input_text, expected):
    inventory_module.patterns['section'] = re.compile(
        r'''^\[
                ([^:\]\s]+)             # group name (see groupname below)
                (?::(\w+))?             # optional : and tag name
            \]
            \s*                         # ignore trailing whitespace
            (?:\#.*)?                   # and/or a comment till the
            $                           # end of the line
        ''', re.X)
    match = inventory_module.patterns['section'].match(input_text)
    assert (match is not None) == expected

# Test that the groupname pattern is compiled correctly
@pytest.mark.parametrize("input_text, expected", [
    ("groupname", True),
    ("somegroup", True),
    ("naughty", True),
    ("groupname:", False),  # Invalid group name (ends with colon)
    ("groupname]", False),   # Invalid group name (contains closing bracket)
    ("groupname comment", False),  # Comment at the end of line
])
def test_groupname_pattern(inventory_module, input_text, expected):
    inventory_module.patterns['groupname'] = re.compile(
        r'''^
                ([^:\]\s]+)
                \s*                         # ignore trailing whitespace
                (?:\#.*)?                   # and/or a comment till the
                $                           # end of the line
            ''', re.X)
    match = inventory_module.patterns['groupname'].match(input_text)
    assert (match is not None) == expected
