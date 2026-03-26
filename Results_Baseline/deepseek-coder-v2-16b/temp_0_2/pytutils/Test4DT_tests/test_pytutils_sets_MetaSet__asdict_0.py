# Module: pytutils.sets
import pytest
import random
import attr
import copy

# Import the function from the module
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_initialization(meta_set):
    assert hasattr(meta_set, '_store'), "MetaSet should have a _store attribute"
    assert isinstance(meta_set._store, set), "_store should be an instance of set"
    assert hasattr(meta_set, '_meta'), "MetaSet should have a _meta attribute"
    assert isinstance(meta_set._meta, dict), "_meta should be an instance of dict"
    assert hasattr(meta_set, '_initial'), "MetaSet should have an _initial attribute"
    assert meta_set._initial is None, "_initial should be initialized to None"

def test_add_value(meta_set):
    initial_length = len(meta_set._store)
    meta_set.add('example_value')
    assert 'example_value' in meta_set._store, "Value not added to the set"
    assert len(meta_set._store) == initial_length + 1, "Set length did not increase after adding a value"
    assert meta_set._meta['example_value'] is not None, "Metadata for added value should be set"

def test_update_values(meta_set):
    meta_set.update([1, 2, 3])
    assert all(x in meta_set._store for x in [1, 2, 3]), "Values not added to the set"
    assert len(meta_set._store) == 3, "Set length does not match the number of updated values"

def test_discard_value(meta_set):
    meta_set.update([1, 2, 3])
    initial_length = len(meta_set._store)
    meta_set.discard(2)
    assert 2 not in meta_set._store, "Value was not discarded from the set"
    assert len(meta_set._store) == initial_length - 1, "Set length did not decrease after discarding a value"

def test_check_membership(meta_set):
    meta_set.update([1, 2, 3])
    assert 2 in meta_set, "Value is present in the set but membership check failed"
    assert 'non_existent_value' not in meta_set, "Non-existent value should not be in the set"

def test_iterate_through_set(meta_set):
    meta_set.update([1, 2, 3])
    iterated_values = [x for x in meta_set]
    assert all(x in iterated_values for x in [1, 2, 3]), "Values not correctly iterated through the set"

def test_length_of_set(meta_set):
    initial_length = len(meta_set._store)
    meta_set.update([1, 2, 3])
    assert len(meta_set) == len(meta_set._store), "Length of the set does not match the actual length"

def test_asdict(meta_set):
    meta_set.update([1, 2, 3])
    meta_set.add('example_value')
    copied_metadata = meta_set._asdict()
    assert isinstance(copied_metadata, dict), "Returned metadata is not a dictionary"
    assert len(copied_metadata) == len(meta_set._meta), "Copied metadata length does not match the original"
