
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_case_single_element():
    single_element_list = ImmutableList(head=1)
    assert len(single_element_list) == 1
