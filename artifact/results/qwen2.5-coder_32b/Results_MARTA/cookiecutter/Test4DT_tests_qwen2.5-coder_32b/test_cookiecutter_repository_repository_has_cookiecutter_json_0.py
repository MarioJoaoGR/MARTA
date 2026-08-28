
import os
import tempfile
import shutil
import pytest

def repository_has_cookiecutter_json(repo_directory):
    """Determine if `repo_directory` contains a `cookiecutter.json` file.

    :param repo_directory: The candidate repository directory.
    :return: True if the `repo_directory` is valid, else False.
    """
    repo_directory_exists = os.path.isdir(repo_directory)

    repo_config_exists = os.path.isfile(
        os.path.join(repo_directory, 'cookiecutter.json')
    )
    return repo_directory_exists and repo_config_exists

@pytest.fixture(scope="function")
def temp_dir():
    """Create a temporary directory for testing."""
    dir_path = tempfile.mkdtemp()
    yield dir_path
    shutil.rmtree(dir_path)

def test_valid_repository(temp_dir):
    """Test a valid repository directory containing 'cookiecutter.json'."""
    cookiecutter_json_path = os.path.join(temp_dir, 'cookiecutter.json')
    with open(cookiecutter_json_path, 'w') as f:
        f.write('{}')  # Create an empty JSON file

    assert repository_has_cookiecutter_json(temp_dir) is True

def test_nonexistent_directory():
    """Test a non-existent directory."""
    nonexistent_path = '/path/to/nonexistent_directory'
    assert repository_has_cookiecutter_json(nonexistent_path) is False

def test_directory_without_cookiecutter_json(temp_dir):
    """Test a directory that does not contain 'cookiecutter.json'."""
    # No file created in temp_dir
    assert repository_has_cookiecutter_json(temp_dir) is False
