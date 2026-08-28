
import re
from typing import Any
import pytest
from string_utils.validation import is_camel_case

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

CAMEL_CASE_TEST_RE = re.compile(r'^[a-zA-Z][a-zA-Z0-9]*$')

def test_is_camel_case_valid():
    assert is_camel_case('myStringWithCamelCase') == True


def test_is_camel_case_invalid_starts_with_number():
    assert is_camel_case('123myStringStartsWithNumber') == False

def test_is_camel_case_empty_string():
    assert is_camel_case('') == False

def test_is_camel_case_only_lowercase_letters():
    assert is_camel_case('onlylowercaseletters') == False