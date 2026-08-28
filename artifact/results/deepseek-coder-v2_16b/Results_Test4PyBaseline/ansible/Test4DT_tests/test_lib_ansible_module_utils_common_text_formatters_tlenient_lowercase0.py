# Module: ansible.module_utils.common.text.formatters
# test_lenient_lowercase.py
from ansible.module_utils.common.text.formatters import lenient_lowercase

def test_basic_usage():
    assert lenient_lowercase(['Hello', 'World', 123]) == ['hello', 'world', 123]

def test_all_strings():
    assert lenient_lowercase(['Python', 'Programming', '42']) == ['python', 'programming', '42']

def test_mixed_types():
    assert lenient_lowercase([1, 2, {'key': 'Value'}]) == [1, 2, {'key': 'Value'}]

def test_empty_list():
    assert lenient_lowercase([]) == []

def test_non_string_only():
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]
