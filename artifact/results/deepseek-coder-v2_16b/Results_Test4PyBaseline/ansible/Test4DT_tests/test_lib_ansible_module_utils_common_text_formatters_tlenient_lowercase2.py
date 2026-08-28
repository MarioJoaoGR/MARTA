
# Module: ansible.module_utils.common.text.formatters
from ansible.module_utils.common.text.formatters import lenient_lowercase

def test_lenient_lowercase_basic():
    """Test basic usage with a list containing strings and non-strings."""
    assert lenient_lowercase(['Hello', 'World', 123]) == ['hello', 'world', 123]

def test_lenient_lowercase_all_strings():
    """Test all elements are strings in the list."""
    assert lenient_lowercase(['Python', 'Programming', '42']) == ['python', 'programming', '42']

def test_lenient_lowercase_mixed_types():
    """Test with a list containing mixed types including non-strings."""
    assert lenient_lowercase([1, 2, {'key': 'Value'}]) == [1, 2, {'key': 'Value'}]

def test_lenient_lowercase_empty_list():
    """Test with an empty list."""
    assert lenient_lowercase([]) == []

def test_lenient_lowercase_non_string_only():
    """Test with a list containing only non-strings."""
    assert lenient_lowercase([1, 2, 3]) == [1, 2, 3]

def test_lenient_lowercase_none_elements():
    """Test with a list containing None elements."""
    assert lenient_lowercase(['Hello', None, 'World']) == ['hello', None, 'world']

def test_lenient_lowercase_non_string_with_strings():
    """Test with a list containing non-strings and strings."""
    assert lenient_lowercase([1, 'Python', 3.14, {'key': 'Value'}]) == [1, 'python', 3.14, {'key': 'Value'}]
