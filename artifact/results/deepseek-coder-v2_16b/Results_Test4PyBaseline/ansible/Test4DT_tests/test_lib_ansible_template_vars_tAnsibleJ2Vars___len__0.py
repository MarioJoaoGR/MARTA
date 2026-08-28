
import pytest
from ansible.template.vars import AnsibleJ2Vars
from jinja2 import Environment

@pytest.fixture
def setup():
    env = Environment()
    globals_dict = {'global_var': 'global value'}
    locals_dict = {'local_var': 'local value'}
    j2vars = AnsibleJ2Vars(templar=env.get_template, globals=globals_dict, locals=locals_dict)
    return j2vars

def test_initialization():
    env = Environment()
    globals_dict = {'global_var': 'global value'}
    locals_dict = {'local_var': 'local value'}
    ansible_j2_vars = AnsibleJ2Vars(templar=env.get_template, globals=globals_dict, locals=locals_dict)
    
    assert hasattr(ansible_j2_vars, '_templar')
    assert hasattr(ansible_j2_vars, '_globals')
    assert hasattr(ansible_j2_vars, '_locals')
    assert ansible_j2_vars._templar == env.get_template
    assert ansible_j2_vars._globals == globals_dict
    assert ansible_j2_vars._locals == locals_dict

def test_len(setup):
    j2vars = setup