
import pytest
from ansible.plugins.lookup import vars as lookup_module
from ansible.errors import AnsibleError, AnsibleUndefinedVariable

# Fixture to create a LookupModule instance for testing
@pytest.fixture
def setup():
    return lookup_module.LookupModule()

# Test scenario 1: test_valid_input_basic
def test_valid_input_basic(setup):
    terms = ["PATH", "HOME"]
    variables = {"PATH": "/usr/bin:/bin"}
    result = setup.run(terms, variables=variables)
    assert len(result) == 2
    assert isinstance(result[0], str) and result[0] == '/usr/bin:/bin'
    assert isinstance(result[1], str) and result[1] == ''

# Test scenario 2: test_error_handling_undefined_variable
def test_error_handling_undefined_variable(setup):
    terms = ["USER", "USERNAME"]
    variables = {"USER": "admin"}
    default_value = "guest"
    result = setup.run(terms, variables=variables, default=default_value)
    assert len(result) == 2
    assert isinstance(result[0], str) and result[0] == 'admin'
    assert isinstance(result[1], str) and result[1] == 'guest'

# Test scenario 3: test_invalid_input_type
def test_invalid_input_type(setup):
    terms = [123]
    variables = {"PATH": "/usr/bin:/bin"}
    with pytest.raises(AnsibleError) as excinfo:
        setup.run(terms, variables=variables)
    assert str(excinfo.value) == 'Invalid setting identifier, "123" is not a string, its a <class \'int\'>'
