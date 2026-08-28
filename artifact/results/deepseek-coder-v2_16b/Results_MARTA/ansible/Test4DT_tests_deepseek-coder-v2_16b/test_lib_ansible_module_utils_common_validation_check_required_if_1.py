
import pytest
from ansible.module_utils.common.validation import check_required_if

def count_terms(term, parameters):
    return sum([1 for t in term if t in parameters])

# Test scenarios
def test_valid_case():
    requirements = [
        ['state', 'present', ('path',)],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {'state': 'present', 'someint': 99}
    assert check_required_if(requirements, parameters) == []

def test_edge_case():
    requirements = None
    parameters = {}
    assert check_required_if(requirements, parameters) == []

def test_error_case():
    requirements = [
        ['state', 'present', ('path',)],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {'state': 'absent'}
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters)
    assert "state is absent but all of the following are missing: path" in str(excinfo.value)
