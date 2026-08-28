
import pytest
from ansible.playbook.role.requirement import RoleRequirement
from ansible.errors import AnsibleError

# Test scenarios
valid_string = 'galaxy.example,1.0'
valid_dict = {'src': 'galaxy.example,1.0'}
invalid_format = 'invalid,format'
none_input = None
empty_dict = {}
invalid_old_style = {'role': 'example,1.0'}
github_role = 'git+https://github.com/example/galaxy.role'
invalid_src_format = {'src': 'invalid,format'}

# Test functions
def test_valid_string_input():
    role = valid_string
    parsed_role = RoleRequirement.role_yaml_parse(role)
    assert isinstance(parsed_role, dict)
    assert 'name' in parsed_role
    assert 'src' in parsed_role
    assert 'scm' in parsed_role
    assert 'version' in parsed_role

def test_valid_dict_input():
    role = valid_dict
    parsed_role = RoleRequirement.role_yaml_parse(role)
    assert isinstance(parsed_role, dict)
    assert 'name' in parsed_role
    assert 'src' in parsed_role
    assert 'scm' in parsed_role
    assert 'version' in parsed_role

def test_invalid_string_format():
    role = invalid_format
    with pytest.raises(AnsibleError):
        RoleRequirement.role_yaml_parse(role)

def test_none_input():
    role = none_input
    with pytest.raises(TypeError):
        RoleRequirement.role_yaml_parse(role)

def test_empty_dict_input():
    role = empty_dict
    parsed_role = RoleRequirement.role_yaml_parse(role)
    assert isinstance(parsed_role, dict)
    assert 'name' in parsed_role
    assert 'src' in parsed_role
    assert 'scm' in parsed_role
    assert 'version' in parsed_role

def test_invalid_old_style_requirement():
    role = invalid_old_style
    with pytest.raises(AnsibleError):
        RoleRequirement.role_yaml_parse(role)

def test_github_role():
    role = github_role
    parsed_role = RoleRequirement.role_yaml_parse(role)
    assert isinstance(parsed_role, dict)
    assert 'name' in parsed_role
    assert 'src' in parsed_role
    assert 'scm' in parsed_role
    assert 'version' in parsed_role

def test_invalid_src_format():
    role = invalid_src_format
    with pytest.raises(AnsibleError):
        RoleRequirement.role_yaml_parse(role)
