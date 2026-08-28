
import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupModule as BaseLookupModule

class LookupModule(BaseLookupModule):
    def run(self, terms, variables=None, **kwargs):
        if variables is None:
            variables = {}
        return super().run(terms, variables, **kwargs)

def test_valid_input_with_variables():
    lookup_module = LookupModule()
    terms = ['{{var1}}', '{{var2}']
    variables = {'var1': 'value1', 'var2': 'value2'}
    result = lookup_module.run(terms, variables=variables)
    assert result == ['value1', 'value2']

def test_empty_terms():
    lookup_module = LookupModule()
    terms = []
    variables = {'var1': 'default_value'}
    with pytest.raises(AnsibleError):
        lookup_module.run(terms, variables=variables)

def test_invalid_variable():
    lookup_module = LookupModule()
    terms = ['{{undefinedVar}}']
    variables = {}
    kwargs = {'fail_on_undefined': True}
    with pytest.raises(AnsibleError):
        lookup_module.run(terms, variables=variables, **kwargs)
