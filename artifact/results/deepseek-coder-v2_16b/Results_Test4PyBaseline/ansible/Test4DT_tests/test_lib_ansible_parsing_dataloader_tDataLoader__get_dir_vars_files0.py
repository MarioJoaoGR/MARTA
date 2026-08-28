# Module: ansible.parsing.dataloader
import pytest
from ansible.parsing.dataloader import DataLoader

# Test case for creating an instance of DataLoader
def test_create_dataloader():
    dl = DataLoader()
    assert isinstance(dl, DataLoader), "DataLoader instance creation failed"

# Test case for loading data from a string
def test_load_from_string():
    dl = DataLoader()
    data_from_string = dl.load('{"key": "value"}')
    assert isinstance(data_from_string, dict), "Data loaded from string is not of type dict"
    assert data_from_string == {"key": "value"}, "Loaded data does not match the expected JSON content"

# Test case for loading data from a file (assuming the file exists and is in the base directory)
def test_load_from_file(tmp_path):
    # Create a temporary file with some YAML content
    yaml_content = """key: value"""
    file_path = tmp_path / "test.yaml"
    file_path.write_text(yaml_content)
    
    dl = DataLoader()
    data_from_file = dl.load_from_file(str(file_path))
    assert isinstance(data_from_file, dict), "Data loaded from file is not of type dict"
    assert data_from_file == {"key": "value"}, "Loaded data does not match the expected YAML content"

# Test case for setting vault password (optional)
def test_set_vault_secrets():
    dl = DataLoader()
    dl.set_vault_secrets('foo')
    assert hasattr(dl, '_vaults'), "Vault secrets were not set correctly"
    assert dl._vaults == {'password': 'foo'}, "Vault password was not set correctly"

# Test case for _get_dir_vars_files method
def test_get_dir_vars_files(tmp_path):
    # Create a temporary directory structure with files and subdirectories
    dir1 = tmp_path / "dir1"
    dir1.mkdir()
    file1 = dir1 / "file1.yaml"
    file1.write_text("key: value")
    
    dl = DataLoader()
    found_files = dl._get_dir_vars_files(str(tmp_path), extensions=['.yaml'])
    assert len(found_files) == 1, "Expected to find one file with .yaml extension"
    assert str(file1) in found_files, "The expected file was not found in the directory structure"

if __name__ == "__main__":
    pytest.main()
