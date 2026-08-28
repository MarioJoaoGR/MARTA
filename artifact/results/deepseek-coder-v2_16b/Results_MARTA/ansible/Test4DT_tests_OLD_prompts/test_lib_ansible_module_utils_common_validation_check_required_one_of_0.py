
import pytest
from ansible.module_utils.common.validation import check_required_one_of



def test_missing_term_with_context():
    terms = [['nested1', 'nested2'], ['foo', 'bar']]
    parameters = {'parent': {'nested1': 1}}
    with pytest.raises(TypeError):
        check_required_one_of(terms, parameters, options_context=['parent'])

def test_no_terms():
    terms = []
    parameters = {'param1': 1, 'param2': 2}
    result = check_required_one_of(terms, parameters)
    assert result == []