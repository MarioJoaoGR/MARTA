
import pytest
from sty import Register

def test_edge_case():
    # Create an instance of the Register class
    reg = Register()
    
    # Call the as_namedtuple method to get a namedtuple representation of the register
    namedtuple_reg = reg.as_namedtuple()
    
    # Check that the result is indeed a namedtuple
    assert isinstance(namedtuple_reg, tuple), "Expected a namedtuple"
    
    # Check that the fields in the namedtuple match the keys of the dictionary returned by as_dict
    d = reg.as_dict()
    expected_fields = d.keys()
    assert list(namedtuple_reg._fields) == list(expected_fields), "Namedtuple fields do not match dictionary keys"
    
    # Check that the values in the namedtuple match the values of the corresponding keys in the dictionary
    for field, value in zip(expected_fields, d.values()):
        assert getattr(namedtuple_reg, field) == value, f"Value mismatch for field {field}"
