
import pytest
from ansible.template.vars import AnsibleJ2Vars
from jinja2 import Environment

@pytest.fixture
def setup():
    env = Environment()
    templar = env.get_template  # Corrected method name from 'templa' to 'get_template'
    globals_dict = {'global_var': 'global value'}
    locals_dict = {'local_var': 'local value'}
    j2vars = AnsibleJ2Vars(templar=templar, globals=globals_dict, locals=locals_dict)
    return j2vars

def test_init():
    env = Environment()
    templar = env.get_template  # Corrected method name from 'templa' to 'get_template'
    globals_dict = {'global_var': 'global value'}
    locals_dict = {'local_var': 'local value'}
    ansible_j2_vars = AnsibleJ2Vars(templar=templar, globals=globals_dict, locals=locals_dict)
    
    assert ansible_j2_vars._templar == templar
    assert ansible_j2_vars._globals == globals_dict
    assert ansible_j2_vars._locals == {'local_var': 'local value'}

def test_getitem(setup):
    j2vars = setup
    # Test accessing existing local variable