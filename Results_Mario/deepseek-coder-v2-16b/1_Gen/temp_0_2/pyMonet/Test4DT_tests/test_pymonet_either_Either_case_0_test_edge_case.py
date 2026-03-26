
import pytest
from pymonet.either import Either, Left, Right

def test_edge_case():
    # Test None input
    either = Either(None)
    
    def handle_error(_):
        return "Error handled"
    
    def handle_success(_):
        return "Success value"
    
    result = either.case(handle_error, handle_success)
    assert result == "Error handled"
