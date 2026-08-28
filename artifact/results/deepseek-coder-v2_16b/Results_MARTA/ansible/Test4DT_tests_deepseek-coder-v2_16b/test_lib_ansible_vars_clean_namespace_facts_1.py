
import pytest
from ansible.vars.clean import module_response_deepcopy

def namespace_facts(facts):
    ''' return all facts inside 'ansible_facts' w/o an ansible_ prefix '''
    deprefixed = {}
    for k in facts:
        if k.startswith('ansible_') and k not in ('ansible_local',):
            deprefixed[k[8:]] = module_response_deepcopy(facts[k])
        else:
            deprefixed[k] = module_response_deepcopy(facts[k])
    return {'ansible_facts': deprefixed}

# Test 1: test_valid_input
def test_valid_input():
    facts = {'ansible_host': 'localhost', 'ansible_user': 'root', 'host': 'localhost', 'user': 'root'}
    result = namespace_facts(facts)
    assert isinstance(result, dict), "Expected a dictionary"
    assert 'ansible_facts' in result, "'ansible_facts' key not found in the result"
    assert len(result['ansible_facts']) == 4, "Expected 4 items in 'ansible_facts'"
    assert result['ansible_facts']['host'] == 'localhost', "Expected host to be 'localhost'"
    assert result['ansible_facts']['user'] == 'root', "Expected user to be 'root'"

# Test 2: test_edge_case_none
def test_edge_case_none():
    facts = None
    with pytest.raises(TypeError):
        namespace_facts(facts)

# Test 3: test_invalid_input
def test_invalid_input():
    facts = 'not a dictionary'
    with pytest.raises(TypeError):
        namespace_facts(facts)
