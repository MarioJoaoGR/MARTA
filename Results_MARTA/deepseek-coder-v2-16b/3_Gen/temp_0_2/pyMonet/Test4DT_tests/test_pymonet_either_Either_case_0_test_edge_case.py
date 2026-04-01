
import pytest
from pymonet.either import Either, Left, Right

def test_edge_case():
    # Test edge case with None as input, expecting Left type
    either = Either(None)
    
    def error_handler(value):
        return "Error!"
    
    def success_handler(value):
        return value + 10
    
    assert either.case(error_handler, success_handler) == "Error!"
