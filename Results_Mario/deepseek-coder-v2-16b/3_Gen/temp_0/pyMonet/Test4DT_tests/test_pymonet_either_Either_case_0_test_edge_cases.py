
import pytest
from pymonet.either import Either, Left, Right

def test_edge_cases():
    # Test with None value
    none_value = Either(Left(None))
    assert none_value.case(lambda x: "Error", lambda x: "Success") == "Error"
    
    # Test with empty list
    empty_list = Either(Right([]))
    assert empty_list.case(lambda x: "Error", lambda x: "Success") == "Error"
