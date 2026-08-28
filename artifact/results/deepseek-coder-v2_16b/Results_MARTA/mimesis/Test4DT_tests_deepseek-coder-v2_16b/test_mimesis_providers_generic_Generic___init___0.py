
import pytest
from mimesis import Generic
from mimesis.providers import Person, Address, Datetime, Business, Text, Food, Science, Transport, Code, UnitSystem, File, Numbers, Development, Hardware, Clothing, Internet, Path, Payment, Cryptographic, Structure, Choice

def test_default_initialization():
    generic_instance = Generic()
    assert isinstance(generic_instance.transport, Transport)
    assert isinstance(generic_instance.code, Code)
    assert isinstance(generic_instance.unit_system, UnitSystem)
    # Add more assertions for other providers if necessary

def test_specific_seed():
    generic_instance = Generic(seed=42)
    assert isinstance(generic_instance.transport, Transport)
    assert isinstance(generic_instance.code, Code)
    assert isinstance(generic_instance.unit_system, UnitSystem)
    # Add more assertions for other providers if necessary
