
import pytest
from mimesis.providers.choice import Choice
import random

# Fixture to create a Choice instance for testing
@pytest.fixture
def choice_instance():
    return Choice()

# Test cases for generating a single random choice from a list
def test_single_random_choice_from_list(choice_instance):
    items = ['a', 'b', 'c']
    result = choice_instance(items=items)
    assert result in items, f"Expected {result} to be one of the items."

# Test cases for generating a sequence of unique elements from a string
def test_sequence_of_unique_elements_from_string(choice_instance):
    items = 'aabbbccccddddd'
    result = choice_instance(items=items, length=4, unique=True)
    assert len(set(result)) == 4, "Expected the sequence to contain only unique elements."
    assert len(result) == 4, "Expected the sequence to have the specified length."

# Test cases for generating a random choice from a tuple
def test_single_random_choice_from_tuple(choice_instance):
    items = ('a', 'b', 'c')
    result = choice_instance(items=items)
    assert result in items, f"Expected {result} to be one of the items."

# Test cases for generating a sequence of random choices with default length (0 implies single element)
def test_default_length_single_element(choice_instance):
    items = ['a', 'b', 'c']
    result = choice_instance(items=items)
    assert isinstance(result, str), "Expected a single uncontained element to be chosen."
    assert result in items, f"Expected {result} to be one of the items."

# Test cases for generating a sequence of unique choices with specified length
def test_sequence_of_unique_choices_with_specified_length(choice_instance):
    items = ['a', 'b', 'c']  # Changed from set to list to satisfy non-empty sequence type requirement
    result = choice_instance(items=items, length=2, unique=True)
    assert len(set(result)) == 2, "Expected the sequence to contain only unique elements."
    assert len(result) == 2, "Expected the sequence to have the specified length."

# Test cases for handling non-sequence items
def test_non_sequence_items():
    choice = Choice()
    with pytest.raises(TypeError):
        choice(items=123)

# Test cases for handling negative length
def test_negative_length():
    choice = Choice()
    with pytest.raises(ValueError):
        choice(items=['a', 'b', 'c'], length=-1)

# Test cases for ensuring the method always returns a list when items are provided as a list
def test_always_return_list():
    choice = Choice()
    result = choice(items=['a', 'b', 'c'], length=3, unique=False)
    assert isinstance(result, list), "Expected the method to always return a list."
