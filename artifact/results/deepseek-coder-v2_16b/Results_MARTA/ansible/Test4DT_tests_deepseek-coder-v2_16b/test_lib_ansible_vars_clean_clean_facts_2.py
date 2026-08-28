
import pytest
from ansible.vars.clean import clean_facts
import copy

def test_valid_input():
    original_facts = {'ansible_os': 'Linux', '_ansible_key1': 'value1', 'nested': {'_ansible_inner_key': 'inner_value'}}
    cleaned_facts = clean_facts(copy.deepcopy(original_facts))
    assert cleaned_facts == {'ansible_os': 'Linux', 'nested': {}}

def test_edge_case():
    invalid_input = None
    with pytest.raises(TypeError):
        clean_facts(invalid_input)

def test_invalid_input():
    invalid_input = 'not a dictionary'
    with pytest.raises(TypeError):
        clean_facts(invalid_input)
