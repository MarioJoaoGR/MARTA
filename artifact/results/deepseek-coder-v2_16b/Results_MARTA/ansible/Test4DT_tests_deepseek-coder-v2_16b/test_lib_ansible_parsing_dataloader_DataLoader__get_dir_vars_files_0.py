
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound, AnsibleParserError

def test_valid_input_load_from_file():
    dl = DataLoader()
    with pytest.raises(AnsibleFileNotFound):
        data_dict = dl.load_from_file('/path/to/config.yaml')

def test_none_input_load():
    dl = DataLoader()
    with pytest.raises(TypeError):
        dl.load(None)

def test_invalid_file_path_load_from_file():
    dl = DataLoader()
    with pytest.raises(AnsibleFileNotFound):
        data_dict = dl.load_from_file('/nonexistent/path')
