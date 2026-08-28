
import pytest
from mimesis.providers.choice import Choice
import random

# Fixture to create a Choice instance for testing
@pytest.fixture
def choice_instance():
    return Choice()

# Test cases for handling non-integer length (should raise TypeError)
def test_non_integer_length(choice_instance):
    items = ['a', 'b', 'c']
    with pytest.raises(TypeError):
        choice_instance(items=items, length='invalid')

# Test cases for handling empty sequence as items (should raise ValueError)
def test_empty_sequence_as_items(choice_instance):
    items = []
    with pytest.raises(ValueError):
        choice_instance(items=items)

# Test cases for ensuring there are enough unique elements to satisfy the length requirement
def test_not_enough_unique_elements(choice_instance):
    items = ['a', 'b']  # Only two unique elements
    with pytest.raises(ValueError):
        choice_instance(items=items, length=3, unique=True)

# Test cases for ensuring the method always returns a list when items are provided as a sequence (even if they are lists)
def test_always_return_list_with_sequence(choice_instance):
    items = ['a', 'b', 'c']
    result = choice_instance(items=items, length=3, unique=False)
    assert isinstance(result, list), "Expected the method to always return a list."

# Test cases for ensuring the method returns the correct type based on the input sequence type (list, tuple, string)
def test_return_type_based_on_sequence_type(choice_instance):
    items = ['a', 'b', 'c']
    result_list = choice_instance(items=items, length=3, unique=False)
    assert isinstance(result_list, list), "Expected the method to return a list when items are provided as a list."
    
    items = ('a', 'b', 'c')
    result_tuple = choice_instance(items=items, length=3, unique=False)
    assert isinstance(result_tuple, tuple), "Expected the method to return a tuple when items are provided as a tuple."
    
    items = 'abc'
    result_str = choice_instance(items=items, length=3, unique=False)
    assert isinstance(result_str, str), "Expected the method to return a string when items are provided as a string."
