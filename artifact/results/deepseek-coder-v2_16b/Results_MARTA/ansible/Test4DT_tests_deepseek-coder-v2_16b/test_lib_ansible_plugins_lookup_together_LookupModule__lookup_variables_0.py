
import pytest
from ansible.plugins.lookup import together

@pytest.fixture(scope="module")
def lookup_module():
    return together._LookupModule()

def test_LookupModule__lookup_variables_basic(lookup_module):
    terms = [[1, 2, 3], [4, 5]]
    result = lookup_module._lookup_variables(terms)
    assert result == [[1, 4], [2, 5], [3, None]]

def test_LookupModule__handle_empty_spots_in_second_array(lookup_module):
    terms = [[1, 2], [3]]
    result = lookup_module._lookup_variables(terms)
    assert result == [[1, 3], [2, None]]

def test_LookupModule__transpose_list_of_arrays(lookup_module):
    terms = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = lookup_module._lookup_variables(terms)
    assert result == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

def test_LookupModule__handle_single_term(lookup_module):
    terms = [[1, 2]]
    result = lookup_module._lookup_variables(terms)
    assert result == [[1, None], [2, None]]
