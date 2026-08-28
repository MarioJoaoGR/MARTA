# Module: thefuck.shells.generic
import pytest
from thefuck.shells import Generic

# Create an instance of the Generic class
generic_instance = Generic()

def test_friendly_name():
    assert generic_instance.friendly_name == 'Generic Shell'

def test_get_aliases():
    aliases = generic_instance.get_aliases()
    assert isinstance(aliases, dict)
    assert len(aliases) == 0
