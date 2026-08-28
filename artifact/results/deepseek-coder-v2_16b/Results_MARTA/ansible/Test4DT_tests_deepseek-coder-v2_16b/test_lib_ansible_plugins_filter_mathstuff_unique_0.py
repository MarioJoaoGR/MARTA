
import pytest
from ansible.errors import AnsibleFilterError

# Assuming HAS_UNIQUE is a global variable that indicates whether the unique filter from Jinja2 or Ansible is available
HAS_UNIQUE = True  # Placeholder for actual availability check

def test_valid_case_no_params():
    result = unique({'var': 'value'}, ['apple', 'banana', 'Apple', 'cherry'])
    assert set(result) == {'apple', 'banana', 'Apple', 'cherry'}

def test_valid_case_with_case_sensitivity():
    result = unique({'var': 'value'}, ['apple', 'banana', 'Apple', 'cherry'], case_sensitive=False)
    assert set(result) == {'apple', 'banana', 'cherry'}

def test_valid_case_with_attribute():
    result = unique({'var': 'value'}, [{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Alice'}], attribute='name')
    assert set(result) == [{'name': 'Alice'}, {'name': 'Bob'}]

def test_valid_case_with_both_params():
    result = unique({'var': 'value'}, ['apple', 'banana', 'Apple', 'cherry'], case_sensitive=False, attribute='name')
    assert set(result) == [{'name': 'Alice'}, {'name': 'Bob'}]

def test_edge_case_empty_list():
    result = unique({'var': 'value'}, [])
    assert result == []

def test_error_case_invalid_params():
    with pytest.raises(AnsibleFilterError):
        unique({'var': 'value'}, ['apple', 'banana', 'Apple', 'cherry'], case_sensitive='invalid', attribute='invalid')
