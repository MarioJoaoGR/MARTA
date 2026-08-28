
import pytest
from pymonet.utils import increase

def test_increase_positive():
    assert increase(5) == 6

def test_increase_negative():
    assert increase(-2) == -1

def test_increase_zero():
    assert increase(0) == 1
