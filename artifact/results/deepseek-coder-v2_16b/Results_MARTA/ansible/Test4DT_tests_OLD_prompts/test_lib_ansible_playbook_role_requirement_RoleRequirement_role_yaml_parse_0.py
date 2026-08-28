
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.role.requirement import RoleRequirement

# Test scenario 1: Basic functionality of role_yaml_parse method
def test_RoleRequirement_role_yaml_parse_basic():
    # Define a basic role specification as a string
    role = "galaxy.example,1.0"
    
    # Call the role_yaml_parse method with the role specification
    parsed_role = RoleRequirement.role_yaml_parse(role)
    
    # Assert that the parsed result is a dictionary and contains expected keys
    assert isinstance(parsed_role, dict), "Parsed role should be a dictionary"
    assert 'name' in parsed_role, "Parsed role should have a name key"
    assert 'src' in parsed_role, "Parsed role should have a src key"
    assert 'scm' in parsed_role, "Parsed role should have a scm key"
    assert 'version' in parsed_role, "Parsed role should have a version key"
    
    # Assert the values of the keys in the parsed dictionary
    assert parsed_role['name'] == RoleRequirement.repo_url_to_role_name("galaxy.example")
    assert parsed_role['src'] == "galaxy.example"
    assert parsed_role['scm'] is None
    assert parsed_role['version'] == "1.0"
