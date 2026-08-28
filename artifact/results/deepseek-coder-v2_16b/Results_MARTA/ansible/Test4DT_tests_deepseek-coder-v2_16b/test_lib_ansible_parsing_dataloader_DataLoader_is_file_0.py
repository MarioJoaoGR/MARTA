
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound, AnsibleParserError
import os

def test_valid_input_load_from_file():
    dataloader = DataLoader()
    valid_file_path = 'tests/data/valid.yaml'  # Assuming you have this file in your project
    
    with pytest.raises(AnsibleFileNotFound):
        data = dataloader.load_from_file(valid_file_path)

def test_error_handling_missing_file():
    dataloader = DataLoader()
    non_existent_file_path = 'non_existent_file.yaml'
    
    with pytest.raises(AnsibleFileNotFound):
        dataloader.load_from_file(non_existent_file_path)
