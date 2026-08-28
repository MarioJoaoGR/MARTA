
import pytest
from apimd.parser import code


def test_empty_input():
    assert code("") == " "
