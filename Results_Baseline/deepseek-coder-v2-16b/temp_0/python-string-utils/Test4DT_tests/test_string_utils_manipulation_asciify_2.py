
# Module: string_utils.manipulation
# test_string_utils_manipulation.py
from string_utils.manipulation import asciify
import pytest
import unicodedata

def is_string(input):
    return isinstance(input, str)

class InvalidInputError(Exception):
    pass

def test_asciify_with_non_ascii_characters():
    input_string = 'èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    expected_output = 'eeuuooaaeynAAACIINOE'
    assert asciify(input_string) == expected_output, f"Expected '{expected_output}' but got '{asciify(input_string)}'"

def test_asciify_with_ascii_characters():
    input_string = 'hello world'
    expected_output = 'hello world'
    assert asciify(input_string) == expected_output, f"Expected '{expected_output}' but got '{asciify(input_string)}'"

def test_asciify_with_mixed_characters():
    input_string = 'hello èéùúòóäåëýñÅÀÁÇÌÍÑÓË world'
    expected_output = 'hello eeuuooaaeynAAACIINOE world'
    assert asciify(input_string) == expected_output, f"Expected '{expected_output}' but got '{asciify(input_string)}'"

def test_asciify_empty_string():
    input_string = ''
    expected_output = ''