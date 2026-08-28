
import pytest
from ansible.template import Templar
from ansible.errors import AnsibleError, AnsibleUndefinedVariable
from ansible.vars.hostvars import HostVars

# Fixture to create a real instance of Templar for testing
@pytest.fixture
def templar():
    return Templar()

# Fixture to create global variables dictionary
@pytest.fixture
def globals_vars():
    return {'global_var': 'global value'}

# Fixture to create local variables dictionary
@pytest.fixture
def locals_vars():
    return {'l_local_var': 'local value', 'other_var': 'other value'}

# Test for valid global variable retrieval
def test_valid_input_global_var(templar, globals_vars):
    j2_vars = AnsibleJ2Vars(templar, globals_vars)
    assert j2_vars['global_var'] == 'global value'

# Test for handling missing local variable
def test_missing_local_var(templar, globals_vars):
    with pytest.raises(KeyError) as e:
        j2_vars = AnsibleJ2Vars(templar, globals_vars)
        assert 'l_local_var' in j2_vars  # This should raise a KeyError
    assert str(e.value) == "undefined variable: l_local_var"

# Test for retrieval of undefined variable
def test_invalid_variable(templar, globals_vars):
    with pytest.raises(KeyError) as e:
        j2_vars = AnsibleJ2Vars(templar, globals_vars)
        assert 'undefined_var' in j2_vars  # This should raise a KeyError
    assert str(e.value) == "undefined variable: undefined_var"
