
import pytest
from ansible.playbook.role.requirement import RoleRequirement

# Test scenarios
def test_valid_input():
    repo_url = 'http://git.example.com/repos/repo.git'
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == 'repo', f"Expected 'repo' but got {role_name}"

def test_edge_case_none():
    repo_url = None
    with pytest.raises(TypeError):
        RoleRequirement().repo_url_to_role_name(repo_url)

def test_invalid_input():
    repo_url = 'invalid-url'
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == 'invalid-url', f"Expected 'invalid-url' but got {role_name}"
