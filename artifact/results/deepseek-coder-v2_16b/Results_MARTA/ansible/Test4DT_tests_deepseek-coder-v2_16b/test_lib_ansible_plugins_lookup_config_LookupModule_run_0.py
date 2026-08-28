
import pytest
from ansible.errors import AnsibleOptionsError, AnsibleLookupError
from unittest.mock import patch

class LookupModule:
    def __init__(self):
        self._options = {}
    
    def set_options(self, var_options=None, direct=None):
        if direct:
            self._options.update(direct)
    
    def get_option(self, key):
        return self._options.get(key)
    
    def run(self, terms, variables=None, **kwargs):
        self.set_options(var_options=variables, direct=kwargs)
        missing = self.get_option('on_missing')
        ptype = self.get_option('plugin_type')
        pname = self.get_option('plugin_name')
        
        if (ptype or pname) and not (ptype and pname):
            raise AnsibleOptionsError('Both plugin_type and plugin_name are required, cannot use one without the other')
        
        if not isinstance(missing, str) or missing not in ['error', 'warn', 'skip']:
            raise AnsibleOptionsError('"on_missing" must be a string and one of "error", "warn" or "skip", not %s' % missing)
        
        ret = []
        for term in terms:
            if not isinstance(term, str):
                raise AnsibleOptionsError('Invalid setting identifier, "%s" is not a string, its a %s' % (term, type(term)))
            
            result = None
            try:
                if pname:
                    result = _get_plugin_config(pname, ptype, term, variables)
                else:
                    result = _get_global_config(term)
            except MissingSetting as e:
                if missing == 'error':
                    raise AnsibleLookupError('Unable to find setting %s' % term, orig_exc=e)
                elif missing == 'warn':
                    self._display.warning('Skipping, did not find setting %s' % term)
                elif missing == 'skip':
                    pass
            
            if result is not None:
                ret.append(result)
        return ret

# Mocking _get_plugin_config and _get_global_config for testing purposes
def _get_plugin_config(pname, ptype, term, variables):
    pass

def _get_global_config(term):
    pass

@pytest.fixture
def lookup_module():
    return LookupModule()

# Test cases
@pytest.mark.parametrize("terms, variables, kwargs, expected_exception", [
    (['setting1', 'setting2'], {'var1': 'val1'}, {'plugin_type': 'lookup', 'plugin_name': 'my_plugin', 'on_missing': 'error'}, None),
    (['setting1', 'setting2'], {'var1': 'val1'}, {}, None),
    (['setting1', 'setting2'], {'var1': 'val1'}, {'plugin_type': 'lookup'}, Exception),
    (['setting1', 'setting2'], {'var1': 'val1'}, {'plugin_name': 'my_plugin'}, Exception),
    (['setting1', 'setting2'], {'var1': 'val1'}, {'on_missing': None}, Exception),
    (['setting1', 'setting2'], {'var1': 'val1'}, {'on_missing': 'invalid'}, Exception),
    (['setting1', 'setting2'], {'var1': 'val1'}, {'terms': 123}, Exception),
    (['setting1', 'setting2'], {'var1': 'val1'}, {'terms': [None]}, Exception),
    ([], {'var1': 'val1'}, {'plugin_type': 'lookup', 'plugin_name': 'my_plugin', 'on_missing': 'error'}, Exception),
    (['setting1', 'setting2'], None, {'plugin_type': 'lookup', 'plugin_name': 'my_plugin', 'on_missing': 'error'}, Exception),
    (['setting1', 'setting2'], {}, {'plugin_type': 'lookup', 'plugin_name': 'my_plugin', 'on_missing': 'error'}, Exception),
])
def test_run(lookup_module, terms, variables, kwargs, expected_exception):
    with pytest.raises(expected_exception) if expected_exception else None:
        lookup_module.run(terms, variables=variables, **kwargs)
