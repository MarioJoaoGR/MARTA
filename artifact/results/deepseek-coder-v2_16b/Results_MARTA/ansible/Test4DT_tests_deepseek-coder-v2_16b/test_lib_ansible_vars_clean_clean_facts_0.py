
import pytest
from ansible.vars.clean import clean_facts



def test_valid_input():
    valid_input = {'ansible_os': 'Linux', '_ansible_key1': 'value1', 'nested': {'_ansible_inner_key': 'inner_value'}}
    expected_output = {'ansible_os': 'Linux', 'nested': {}}
    assert clean_facts(valid_input) == expected_output