
import pytest
from pymonet.immutable_list import ImmutableList

def test_invalid_lambda():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=None))
    
    # Invalid lambda function that always returns False
    invalid_lambda = lambda x: False
    
    result = lst.find(invalid_lambda)
    
    assert result is None
