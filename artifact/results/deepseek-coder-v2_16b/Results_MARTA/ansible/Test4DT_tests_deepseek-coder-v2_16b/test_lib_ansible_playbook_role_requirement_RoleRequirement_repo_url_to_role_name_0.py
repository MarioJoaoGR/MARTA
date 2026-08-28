
import pytest
from ansible.playbook.role.requirement import RoleRequirement

# Scenario 1: Test standard input with a typical HTTP URL
def test_valid_input_http_url():
    repo_url = 'http://git.example.com/repos/repo.git'
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == 'repo', f"Expected 'repo', but got {role_name}"

# Scenario 2: Test standard input with a typical HTTPS URL
def test_valid_input_https_url():
    repo_url = 'https://github.com/user/repo.git'
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == 'repo', f"Expected 'repo', but got {role_name}"

# Scenario 3: Test standard input with a URL containing .tar.gz extension
def test_valid_input_tar_gz():
    repo_url = 'http://git.example.com/repos/another-repo,v1.0.tar.gz'
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == 'another-repo', f"Expected 'another-repo', but got {role_name}"

# Scenario 4: Test standard input with a local file path URL
def test_valid_input_file_path():
    repo_url = 'file:///local/path/to/role'
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == 'role', f"Expected 'role', but got {role_name}"

# Scenario 5: Test handling of None input
def test_invalid_input_none():
    repo_url = None
    with pytest.raises(TypeError):
        RoleRequirement().repo_url_to_role_name(repo_url)

# Scenario 6: Test handling of empty string input
def test_invalid_input_empty_string():
    repo_url = ''
    role_name = RoleRequirement().repo_url_to_role_name(repo_url)
    assert role_name == '', f"Expected an empty string, but got {role_name}"
