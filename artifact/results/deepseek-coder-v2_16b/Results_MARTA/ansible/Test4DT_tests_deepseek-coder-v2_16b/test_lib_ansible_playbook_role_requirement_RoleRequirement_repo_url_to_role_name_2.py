
import pytest
from ansible.playbook.role.requirement import RoleRequirement

def test_repo_url_to_role_name_valid():
    repo_url = "http://git.example.com/repos/repo.git"
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == "repo"

def test_repo_url_to_role_name_github():
    repo_url = "https://github.com/user/repo.git"
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == "repo"

def test_repo_url_to_role_name_comma():
    repo_url = "http://git.example.com/repos/another-repo,v1.0.tar.gz"
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == "another-repo"

def test_repo_url_to_role_name_local():
    repo_url = "file:///local/path/to/role"
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == "role"

def test_repo_url_to_role_name_none():
    repo_url = None
    with pytest.raises(TypeError):
        RoleRequirement().repo_url_to_role_name(repo_url)
