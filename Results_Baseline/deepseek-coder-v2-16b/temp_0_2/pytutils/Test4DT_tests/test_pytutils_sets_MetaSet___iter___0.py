
# Module: pytutils.sets
import pytest
from pytutils.sets import MetaSet
import time
import random
import attr

# Fixture to create a new instance of MetaSet for each test
@pytest.fixture
def meta_set():
    return MetaSet()

# Test initialization without initial values
def test_initialization_without_initial_values(meta_set):
    assert list(meta_set) == []

# Test adding a single value to the set
def test_add_single_value(meta_set):
    meta_set.add(1)
    assert list(meta_set) == [1]

# Test adding multiple values to the set using `update`
def test_update_multiple_values(meta_set):
    meta_set.update([1, 2, 3])
    assert list(meta_set) == [1, 2, 3]

# Test discarding an element from the set
def test_discard_element(meta_set):
    meta_set.update([1, 2, 3])
    meta_set.discard(2)
    assert list(meta_set) == [1, 3]

# Test checking if an element is in the set
def test_check_membership(meta_set):
    meta_set.update([1, 2, 3])
    assert 2 in meta_set

# Test iterating through the set
def test_iteration(meta_set):
    meta_set.update([1, 2, 3])
    result = [value for value in meta_set]