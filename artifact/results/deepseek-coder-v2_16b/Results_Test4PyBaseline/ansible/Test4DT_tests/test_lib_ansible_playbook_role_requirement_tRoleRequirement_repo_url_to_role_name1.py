
import pytest
from ansible.playbook.role.requirement import RoleRequirement

# Test cases for repo_url_to_role_name function
def test_repo_url_to_role_name_empty():
    repo_url = ""
    assert RoleRequirement.repo_url_to_role_name(repo_url) == "", f"Expected empty string, but got {RoleRequirement.repo_url_to_role_name(repo_url)}"

def test_repo_url_to_role_name_no_protocol():
    repo_url = "git.example.com/repos/role-name.git"