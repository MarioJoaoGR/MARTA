# Module: pymonet.semigroups
# test_semigroup.py
from pymonet.semigroups import One
import pytest

@pytest.fixture
def one_false():
    return One(False)

@pytest.fixture
def one_true():
    return One(True)

def test_initialization_with_false(one_false):
    assert not one_false.value

def test_initialization_with_true(one_true):
    assert one_true.value

def test_concatenation_with_true(one_false, one_true):
    combined = one_false.concat(one_true)
    assert combined.value

def test_concatenation_with_false(one_false, one_true):
    combined = one_true.concat(one_false)
    assert combined.value

def test_concatenation_with_another_false(one_false):
    one1 = One(False)
    one2 = One(False)
    last_combination = one1.concat(one2)  # Combining with a False value
    assert not last_combination.value
