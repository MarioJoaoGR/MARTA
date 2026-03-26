
import pytest
from pymonet.immutable_list import ImmutableList

def test_invalid_lambda():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=None))
    result = lst.find(lambda x: False)  # Always returns False, so no element should be found
    assert result is None
