
import pytest
from sty.primitive import Register

def test_invalid_inputs():
    # Create an instance of the Register class
    register = Register()
    
    # Call the as_namedtuple method and check if it returns a namedtuple
    style_register = register.as_namedtuple()
    
    # Check that the returned object is indeed a namedtuple
    assert isinstance(style_register, tuple), "Expected a namedtuple but got something else"
    
    # Check that the keys of the namedtuple match the keys in the dictionary
    d = register.as_dict()
    expected_keys = set(d.keys())
    actual_keys = set(style_register._fields)
    assert expected_keys == actual_keys, "Keys in the namedtuple do not match the original dictionary keys"
    
    # Check that the values of the namedtuple match the string representations of the register values
    for key, value in d.items():
        assert getattr(style_register, key) == value, f"Value mismatch for key {key}"
