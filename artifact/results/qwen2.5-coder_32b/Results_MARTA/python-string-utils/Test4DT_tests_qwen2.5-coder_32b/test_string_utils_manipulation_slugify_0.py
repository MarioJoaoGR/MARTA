
import re
from string_utils.manipulation import slugify


def test_slugify_with_custom_separator():
    input_string = 'Hello, World! This is a test.'
    separator = '_'
    expected_output = 'hello_world_this_is_a_test'
    assert slugify(input_string, separator) == expected_output

def test_slugify_with_special_characters():
    input_string = 'Top 10 Reasons To Love Dogs!!!'
    expected_output = 'top-10-reasons-to-love-dogs'
    assert slugify(input_string) == expected_output

def test_slugify_with_non_ascii_characters():
    input_string = 'Mönstér Mägnët'
    expected_output = 'monster-magnet'
    assert slugify(input_string) == expected_output

def test_slugify_with_multiple_spaces():
    input_string = 'Multiple   spaces   here'
    expected_output = 'multiple-spaces-here'
    assert slugify(input_string) == expected_output

def test_slugify_with_leading_and_trailing_punctuation():
    input_string = '!!!Leading and trailing punctuation!!!'
    expected_output = 'leading-and-trailing-punctuation'
    assert slugify(input_string) == expected_output

def test_slugify_with_empty_string():
    input_string = ''
    expected_output = ''
    assert slugify(input_string) == expected_output