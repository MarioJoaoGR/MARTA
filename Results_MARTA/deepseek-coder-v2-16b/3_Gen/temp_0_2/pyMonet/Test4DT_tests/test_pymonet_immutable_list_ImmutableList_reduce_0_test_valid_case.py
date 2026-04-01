
import pytest
from pymonet.immutable_list import ImmutableList

def add_to_acc(acc, val):
    return acc + val

@pytest.fixture
def setup():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    return lst

def test_valid_case(setup):
    assert setup.reduce(add_to_acc, 0) == 6  # Expected output: 6 (1 + 2 + 3)
