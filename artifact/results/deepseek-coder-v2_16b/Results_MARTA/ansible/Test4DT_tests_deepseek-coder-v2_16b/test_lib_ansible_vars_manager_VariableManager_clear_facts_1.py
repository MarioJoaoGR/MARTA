
import pytest
from ansible.vars.manager import VariableManager
from unittest.mock import patch
import os
from hashlib import sha1
from collections import defaultdict

@pytest.fixture(scope="module")
def variable_manager():
    return VariableManager()




def test_clear_facts(variable_manager):
    hostname = 'test_host'
    variable_manager._fact_cache[hostname] = {'os': 'Linux', 'kernel': '3.10'}
    assert len(variable_manager._fact_cache) == 1
    
    variable_manager.clear_facts(hostname)
    assert hostname not in variable_manager._fact_cache