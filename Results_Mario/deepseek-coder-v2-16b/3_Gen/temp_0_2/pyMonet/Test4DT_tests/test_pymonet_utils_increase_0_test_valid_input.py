
import pytest
from pymonet.utils import increase

def test_valid_input():
    assert increase(5) == 6
    assert increase(-1) == 0
