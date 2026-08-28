
import pytest
from unittest.mock import patch
from ansible.vars.clean import namespace_facts



def test_missing_ansible_prefix():
    facts = {'host': 'localhost', 'user': 'root'}
    result = namespace_facts(facts)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert 'ansible_facts' in result, "The result should contain 'ansible_facts'"
    assert len(result['ansible_facts']) == 2, "There should be two items after deprefixing"