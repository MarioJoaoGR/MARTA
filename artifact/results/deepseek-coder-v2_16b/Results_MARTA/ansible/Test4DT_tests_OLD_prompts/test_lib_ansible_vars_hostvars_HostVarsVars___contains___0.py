
import pytest
from ansible.vars.hostvars import HostVarsVars
from unittest.mock import MagicMock, patch

def test_contains_method():
    # Create a mock variables dictionary and loader
    vars = {'var1': 'value1', 'var2': 'value2'}
    loader = MagicMock()
    
    # Instantiate the HostVarsVars class with the mocked data
    host_vars = HostVarsVars(vars, loader)
    
    # Test if a variable is contained within the dictionary
    assert 'var1' in host_vars
    assert 'non_existent_var' not in host_vars

