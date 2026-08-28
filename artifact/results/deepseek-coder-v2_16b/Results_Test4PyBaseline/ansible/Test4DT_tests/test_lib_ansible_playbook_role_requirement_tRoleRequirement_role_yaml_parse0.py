
# Module: ansible.playbook.role.requirement
# test_role_requirement.py
from ansible.errors import AnsibleError  # Corrected import and variable name
import pytest
from ansible.playbook.role.requirement import RoleRequirement

def test_role_yaml_parse_string():
    # Test parsing a string with valid format
    role = "galaxy.example,1.0"
    expected_output = {'name': 'galaxy.example', 'src': 'galaxy.example', 'scm': None, 'version': '1.0'}
    assert RoleRequirement().role_yaml_parse(role) == expected_output

def test_role_yaml_parse_dict():
    # Test parsing a dictionary with valid format
    role = {'src': 'galaxy.example,1.0'}
    expected_output = {'name': 'galaxy.example', 'src': 'galaxy.example', 'scm': None, 'version': '1.0'}
    assert RoleRequirement().role_yaml_parse(role) == expected_output

def test_role_yaml_parse_invalid_string():
    # Test parsing an invalid string format
    role = "invalid,format"
    with pytest.raises(AnsibleError):  # Corrected the exception handling
        RoleRequirement().role_yaml_parse(role)

def test_role_yaml_parse_dict_with_extra_keys():
    # Test parsing a dictionary with extra keys that should be ignored
    role = {'src': 'galaxy.example,1.0', 'extra_key': 'extra_value'}
    expected_output = {'name': 'galaxy.example', 'src': 'galaxy.example', 'scm': None, 'version': '1.0'}
    assert RoleRequirement().role_yaml_parse(role) == expected_output

def test_role_yaml_parse_string_with_name():
    # Test parsing a string with name specified
    role = "galaxy.example,1.0,example_role"
    expected_output = {'name': 'example_role', 'src': 'galaxy.example', 'scm': None, 'version': '1.0'}
    assert RoleRequirement().role_yaml_parse(role) == expected_output

def test_role_yaml_parse_string_with_scm():
    # Test parsing a string with scm specified
    role = "git+https://github.com/example/repo"
    expected_output = {'name': 'repo', 'src': 'https://github.com/example/repo', 'scm': 'git', 'version': None}
    assert RoleRequirement().role_yaml_parse(role) == expected_output
