
import pytest
from apimd.parser import code



def test_empty_input():
    doc = ""
    expected_output = " "
    assert code(doc) == expected_output