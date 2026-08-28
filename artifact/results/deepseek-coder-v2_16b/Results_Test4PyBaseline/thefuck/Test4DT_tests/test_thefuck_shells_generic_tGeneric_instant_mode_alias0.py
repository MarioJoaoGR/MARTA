
import pytest
from thefuck.shells.generic import Generic
from warnings import warn

# Test initialization of Generic class
def test_generic_initialization():
    generic_instance = Generic()
    assert hasattr(generic_instance, 'friendly_name')