
import pytest
from mimesis import Generic
from mimesis.providers.generic import Person, Address, Datetime, Business, Text, Food, Science, Transport, Code, UnitSystem, File, Numbers, Development, Hardware, Clothing, Internet, Path, Payment, Cryptographic, Structure, Choice


def test_generic_dir():
    generic_instance = Generic()
    
    expected_attributes = [
        'person', 'address', 'datetime', 'business', 'text', 'food', 
        'science', 'transport', 'code', 'unit_system', 'file', 'numbers', 
        'development', 'hardware', 'clothing', 'internet', 'path', 
        'payment', 'cryptographic', 'structure', 'choice'
    ]
    
    assert sorted(generic_instance.__dir__()) == sorted(expected_attributes)