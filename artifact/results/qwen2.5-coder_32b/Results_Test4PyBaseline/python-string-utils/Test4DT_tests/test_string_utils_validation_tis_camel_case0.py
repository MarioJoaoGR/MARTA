# Module: string_utils.validation
import pytest
from string_utils.validation import is_camel_case

def test_is_camel_case_valid():
    assert is_camel_case('MyString') == True, "Should be camel case"
    assert is_camel_case('ThisIsACamelCaseString') == True, "Should be camel case"
    assert is_camel_case('AnotherExample123') == True, "Should be camel case with numbers"

def test_is_camel_case_invalid_start_with_number():
    assert is_camel_case('1stString') == False, "Should not start with a number"
    assert is_camel_case('9Lives') == False, "Should not start with a number"

def test_is_camel_case_invalid_no_uppercase():
    assert is_camel_case('mystring') == False, "Should contain uppercase letters"
    assert is_camel_case('anotherexample') == False, "Should contain uppercase letters"

def test_is_camel_case_invalid_no_lowercase():
    assert is_camel_case('MYSTRING') == False, "Should contain lowercase letters"
    assert is_camel_case('ANOTHEREXAMPLE') == False, "Should contain lowercase letters"

def test_is_camel_case_invalid_special_characters():
    assert is_camel_case('My_String') == False, "Should not contain underscores"
    assert is_camel_case('This-Is-Camel-Case') == False, "Should not contain hyphens"
    assert is_camel_case('This Is Camel Case') == False, "Should not contain spaces"

def test_is_camel_case_invalid_empty_string():
    assert is_camel_case('') == False, "Empty string should not be camel case"
    assert is_camel_case('   ') == False, "String with only spaces should not be camel case"

def test_is_camel_case_invalid_non_string_input():
    assert is_camel_case(None) == False, "None should not be considered camel case"
    assert is_camel_case(12345) == False, "Integer should not be considered camel case"
    assert is_camel_case(['MyString']) == False, "List should not be considered camel case"
    assert is_camel_case({'key': 'value'}) == False, "Dictionary should not be considered camel case"
