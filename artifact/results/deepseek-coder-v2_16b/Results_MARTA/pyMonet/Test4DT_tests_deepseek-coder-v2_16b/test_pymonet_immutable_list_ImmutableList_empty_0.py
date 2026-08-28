
import pytest
from pymonet.immutable_list import ImmutableList

def test_create_empty_list():
    my_list = ImmutableList(is_empty=True)
    assert my_list.is_empty is True
