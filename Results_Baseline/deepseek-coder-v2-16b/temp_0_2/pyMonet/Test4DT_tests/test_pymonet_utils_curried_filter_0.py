
import pytest
from pymonet.utils import curried_filter

# Test cases for curried_filter function

def test_curried_filter_with_lambda():
    # Define a lambda function to filter even numbers
    filterer = lambda x: x % 2 == 0
    
    # Define the collection of elements
    collection = [1, 2, 3, 4]
    
    # Call the curried_filter function with the lambda function and the collection
    filtered_collection = curried_filter(filterer, collection)
    
    # Assert that the filtered collection contains only even numbers
    assert filtered_collection == [2, 4]

def test_curried_filter_with_predefined_function():
    # Define a function to filter out vowels
    def is_vowel(char):
        return char.lower() in 'aeiou'
    
    # Define the collection of elements
    collection = ['a', 'b', 'c', 'd']
    
    # Call the curried_filter function with the predefined filtering function and the collection
    filtered_collection = curried_filter(is_vowel, collection)
    
    # Assert that the filtered collection contains only vowels