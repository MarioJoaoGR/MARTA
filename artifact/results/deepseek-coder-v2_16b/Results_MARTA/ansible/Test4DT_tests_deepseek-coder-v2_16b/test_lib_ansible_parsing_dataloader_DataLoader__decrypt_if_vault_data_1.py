
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound, AnsibleParserError

def test_invalid_input_load_from_file():
    dl = DataLoader()
    with pytest.raises(AnsibleFileNotFound):
        data = dl.load_from_file('/path/to/nonexistent_file.yaml')
