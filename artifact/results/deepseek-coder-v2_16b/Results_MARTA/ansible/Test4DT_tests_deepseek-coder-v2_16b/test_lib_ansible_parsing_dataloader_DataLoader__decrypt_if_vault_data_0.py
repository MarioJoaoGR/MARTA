
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound, AnsibleParserError

# Test for loading a valid file without vault encryption
def test_valid_input_load_from_file(tmp_path):
    # Create a temporary valid configuration file
    config_file = tmp_path / "config.yaml"
    config_file.write_text("key: value")
    
    dataloader = DataLoader()
    data = dataloader.load_from_file(str(config_file))
    
    assert isinstance(data, dict)
    assert data == {'key': 'value'}

# Test for loading an invalid file path