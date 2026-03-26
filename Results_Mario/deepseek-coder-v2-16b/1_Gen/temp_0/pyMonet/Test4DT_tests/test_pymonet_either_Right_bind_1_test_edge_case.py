
import pytest
from pymonet.either import Right

def test_edge_case():
    right_instance = Right(None)
    mapped_value = right_instance.bind(lambda x: x + 10 if x is not None else None)
    
    assert mapped_value == None
