# Module: ansible.playbook.role.requirement
import pytest
from ansible.playbook.role.requirement import RoleRequirement

# Test cases for repo_url_to_role_name function
def test_repo_url_to_role_name_http():
    repo_url = "http://git.example.com/repos/role-name.git"
    assert RoleRequirement.repo_url_to_role_name(repo_url) == "role-name"

def test_repo_url_to_role_name_https():
    repo_url = "https://github.com/user/role-name.git"
    assert RoleRequirement.repo_url_to_role_name(repo_url) == "role-name"

def test_repo_url_to_role_name_comma():
    repo_url = "http://example.com/path/to/role-name,otherpart"
    assert RoleRequirement.repo_url_to_role_name(repo_url) == "role-name"

def test_repo_url_to_role_name_tar_gz():
    repo_url = "file:///local/path/to/role-name.tar.gz"
    assert RoleRequirement.repo_url_to_role_name(repo_url) == "role-name"

def test_repo_url_to_role_name_ssh():
    repo_url = "git@github.com:user/role-name.git"
    assert RoleRequirement.repo_url_to_role_name(repo_url) == "role-name"

def test_repo_url_to_role_name_simple_string():
    repo_url = "example-string"
    assert RoleRequirement.repo_url_to_role_name(repo_url) == "example-string"

# Additional edge cases can be added to cover more scenarios
