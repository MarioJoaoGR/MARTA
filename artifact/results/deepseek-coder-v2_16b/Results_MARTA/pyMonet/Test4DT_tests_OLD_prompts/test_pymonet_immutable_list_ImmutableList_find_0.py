
import pytest
from unittest.mock import patch
from pymonet.immutable_list import ImmutableList


def test_single_element_not_found():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    result = immutable_list.find(lambda x: x > 2)
    assert result == 3, "Expected the first element that satisfies the condition"
