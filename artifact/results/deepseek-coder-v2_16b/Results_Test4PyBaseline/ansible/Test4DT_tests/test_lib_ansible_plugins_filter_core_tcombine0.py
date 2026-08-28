
import pytest
from ansible.plugins.filter.core import combine
from ansible.errors import AnsibleFilterError

# Test cases for the `combine` function
def test_combine_basic():
    assert combine({'a': 1, 'b': [2]}, {'a': 3, 'c': 4}) == {'a': 3, 'b': [2], 'c': 4}

def test_combine_list_merge():
    result = combine({'a': [1, 2], 'b': {}}, {'a': [3, 4], 'list_merge': 'merge'})
    assert result == {'a': [3, 4, 1, 2], 'b': {}, 'list_merge': 'merge'}

def test_combine_recursive():
    assert combine({'a': {}}, recursive=True) == {'a': {}}

def test_combine_invalid_keyword():
    with pytest.raises(AnsibleFilterError):
        combine({'a': 1}, recursive=True, extra_arg='extra')
