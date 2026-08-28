
import pytest
from ansible.plugins.filter.core import combine
from ansible.errors import AnsibleFilterError

# Test cases for the `combine` function
def test_combine_invalid_keyword():
    with pytest.raises(AnsibleFilterError):
        combine({'a': 1}, recursive=True, extra_arg='extra')

def test_combine_no_terms():
    assert combine() == {}

def test_combine_single_dict():
    assert combine({'a': 1}) == {'a': 1}

def test_combine_multiple_dicts():
    result = combine({'a': 1, 'b': {}}, {'a': 2, 'c': 3}, recursive=True)
    assert result == {'a': 2, 'b': {}, 'c': 3}

def test_combine_list_merge_replace():
    result = combine({'a': [1, 2], 'b': {}}, {'a': [3, 4], 'list_merge': 'replace'})
    assert result == {'a': [3, 4], 'b': {}, 'list_merge': 'replace'}

def test_combine_list_merge_keep():
    result = combine({'a': [1, 2], 'b': {}}, {'a': [3, 4], 'list_merge': 'keep'})