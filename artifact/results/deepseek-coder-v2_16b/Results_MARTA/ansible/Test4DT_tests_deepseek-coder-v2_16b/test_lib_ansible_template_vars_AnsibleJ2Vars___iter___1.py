
import pytest
from ansible.template import Templar
from ansible.vars.manager import VariableManager

class AnsibleJ2Vars:
    '''
    Helper class to template all variable content before Jinja2 sees it. This is done by hijacking the variable storage that Jinja2 uses, and overriding `__contains__` and `__getitem__` to look like a dict. Added bonus is avoiding duplicating the large hashes that inject tends to be.
    
    To facilitate using built-in Jinja2 things like range, globals are also handled here.

    Parameters:
        templar (Templar): A valid Templar() object used for template processing.
        globals (dict): A dictionary of global variables.
        locals (dict, optional): A dictionary of local variables. Defaults to an empty dictionary.
    
    Example:
        ```python
        from ansible.template import Templar
        
        # Define the templar object and global/local variables
        templar = Templar()
        globals_vars = {'global_var': 'value'}
        locals_vars = {'l_local_var': 'value', 'other_var': 'value'}
        
        # Initialize the AnsibleJ2Vars class with the defined objects
        j2_vars = AnsibleJ2Vars(templar, globals_vars, locals_vars)
        ```
    
    This class is designed to provide a bridge between the variables used in an Ansible playbook and the Jinja2 templating engine. By hijacking the variable storage mechanism, it allows for seamless integration of custom variables while maintaining compatibility with standard Jinja2 operations. The `__iter__` method specifically returns an iterator over the set of available variables, local variables, and global variables within the current context, facilitating easy iteration and access to these variables during template processing.
    '''
    def __init__(self, templar, globals, locals=None):
        '''
        Initializes this object with a valid Templar() object, as well as several dictionaries of variables representing different scopes (in Jinja2 terminology).
        '''
        self._templar = templar
        self._globals = globals
        self._locals = dict()
        if isinstance(locals, dict):
            for key, val in locals.items():
                if val is not None:
                    if key[:2] == 'l_':
                        self._locals[key[2:]] = val
                    elif key not in ('context', 'environment', 'template'):
                        self._locals[key] = val

    def __iter__(self):
        keys = set()
        keys.update(self._templar.available_variables, self._locals, self._globals)
        return iter(keys)

# Fixture to create a real instance of AnsibleJ2Vars for testing
@pytest.fixture
def ansible_j2vars():
    templar = Templar()
    globals_vars = {'global_var': 'value'}
    locals_vars = {'l_local_var': 'value', 'other_var': 'value'}
    return AnsibleJ2Vars(templar, globals_vars, locals_vars)

# Test scenarios
def test_valid_input_happy_path(ansible_j2vars):
    assert 'global_var' in ansible_j2vars
    assert ansible_j2vars['global_var'] == 'value'
    assert 'l_local_var' in ansible_j2vars._locals
    assert ansible_j2vars._locals['l_local_var'] == 'value'
    assert 'other_var' in ansible_j2vars._locals
    assert ansible_j2vars._locals['other_var'] == 'value'

def test_edge_case_none_inputs():
    templar = Templar()
    globals_vars = None
    locals_vars = None
    with pytest.raises(TypeError):
        AnsibleJ2Vars(templar, globals_vars, locals_vars)

def test_invalid_input_error_handling():
    templar = "Invalid Templar"
    globals_vars = {}
    locals_vars = {'l_local_var': 'value'}
    with pytest.raises(TypeError):
        AnsibleJ2Vars(templar, globals_vars, locals_vars)
