# Module: ansible.plugins.lookup.nested
# Import the function from the module
from ansible.plugins.lookup import LookupModule
import pytest
from ansible.errors import AnsibleUndefinedVariable

# Fixture to create an instance of LookupModule for testing
@pytest.fixture
def lookup_module():
    return LookupModule()

# Test cases for _lookup_variables method
def test__lookup_variables_basic(lookup_module):
    terms = ["{{var1}}", "{{var2}}"]
    variables = {"var1": "value1", "var2": "value2"}
    results = lookup_module._lookup_variables(terms, variables)
    assert len(results) == 2
    assert isinstance(results[0], list)
    assert isinstance(results[1], list)

def test__lookup_variables_undefined(lookup_module):
    terms = ["{{var1}}", "{{var3}}"]
    variables = {"var1": "value1", "var2": "value2"}
    with pytest.raises(AnsibleUndefinedVariable):
        lookup_module._lookup_variables(terms, variables)

def test__lookup_variables_empty_terms(lookup_module):
    terms = []
    variables = {"var1": "value1", "var2": "value2"}
    results = lookup_module._lookup_variables(terms, variables)
    assert len(results) == 0

def test__lookup_variables_no_variables(lookup_module):
    terms = ["{{var1}}", "{{var2}}"]
    variables = {}
    with pytest.raises(AnsibleUndefinedVariable):
        lookup_module._lookup_variables(terms, variables)
