
# Test case  
# Module: pysnooper.tracer
import pytest
from pysnooper.tracer import UnavailableSource

def test_unavailable_source_getitem():
    unavailable = UnavailableSource()
    
    # Test with zero index
    assert unavailable[0] == 'SOURCE IS UNAVAILABLE', "Index 0 should return 'SOURCE IS UNAVAILABLE'"
    
    # Test with a positive integer index
    assert unavailable[10] == 'SOURCE IS UNAVAILABLE', "Index 10 should return 'SOURCE IS UNAVAILABLE'"
    
    # Test with a large integer index
    assert unavailable[1000] == 'SOURCE IS UNAVAILABLE', "Large index should return 'SOURCE IS UNAVAILABLE'"
    
    # Test with negative index
    assert unavailable[-1] == 'SOURCE IS UNAVAILABLE', "Negative index -1 should return 'SOURCE IS UNAVAILABLE'"

def test_unavailable_source_getitem_with_non_integer():
    unavailable = UnavailableSource()
    
    # Test with a float index
    assert unavailable[0.5] == 'SOURCE IS UNAVAILABLE', "Float index should return 'SOURCE IS UNAVAILABLE'"
    
    # Test with a string index
    assert unavailable['test'] == 'SOURCE IS UNAVAILABLE', "String index should return 'SOURCE IS UNAVAILABLE'"
    
    # Test with None as index
    assert unavailable[None] == 'SOURCE IS UNAVAILABLE', "None index should return 'SOURCE IS UNAVAILABLE'"

def test_unavailable_source_getitem_with_large_negative_index():
    unavailable = UnavailableSource()
    
    # Test with a large negative index
    assert unavailable[-1000] == 'SOURCE IS UNAVAILABLE', "Large negative index should return 'SOURCE IS UNAVAILABLE'"
