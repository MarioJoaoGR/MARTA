
# Module: ansible.module_utils.common.validation
# test_check_type_raw.py
from ansible.module_utils.common.validation import check_type_raw

def test_check_type_raw_integer():
    assert check_type_raw(42) == 42

def test_check_type_raw_string():
    assert check_type_raw("hello") == "hello"

def test_check_type_raw_list():
    assert check_type_raw([1, 2, 3]) == [1, 2, 3]

def test_check_type_raw_dict():
    assert check_type_raw({'key': 'value'}) == {'key': 'value'}

def test_check_type_raw_none():
    assert check_type_raw(None) is None

# Additional test cases for different types of strings
def test_check_type_raw_empty_string():
    assert check_type_raw("") == ""

def test_check_type_raw_special_characters():
    assert check_type_raw("!@#$%^&*()") == "!@#$%^&*()"

def test_check_type_raw_long_string():
    long_string = "a" * 1000
    assert check_type_raw(long_string) == long_string
