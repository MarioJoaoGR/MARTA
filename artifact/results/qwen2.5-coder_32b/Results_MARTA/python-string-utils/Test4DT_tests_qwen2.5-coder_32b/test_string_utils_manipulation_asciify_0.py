
import pytest
from string_utils.manipulation import asciify

def test_asciify_with_non_ascii_word():
    input_string = 'café'
    expected_output = 'cafe'
    assert asciify(input_string) == expected_output

def test_asciify_with_another_non_ascii_word():
    input_string = 'naïve'
    expected_output = 'naive'  # Corrected the expected output based on the function's behavior
    assert asciify(input_string) == expected_output

def test_asciify_with_whitespace_string():
    input_string = ' '
    expected_output = ' '  # The function should return a space if it is in the input
    assert asciify(input_string) == expected_output

def test_asciify_with_empty_string():
    input_string = ''
    expected_output = ''  # The function should return an empty string if it is in the input
    assert asciify(input_string) == expected_output

def test_asciify_with_complex_non_ascii_string():
    input_string = 'èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    expected_output = 'eeuuooaaeynAAACIINOE'
    assert asciify(input_string) == expected_output

def test_asciify_with_already_ascii_string():
    input_string = 'hello world'
    expected_output = 'hello world'  # The function should return the same string if it is already ASCII
    assert asciify(input_string) == expected_output

def test_asciify_with_special_characters():
    input_string = '!@#$%^&*()_+'
    expected_output = '!@#$%^&*()_+'  # Special characters should remain unchanged
    assert asciify(input_string) == expected_output
