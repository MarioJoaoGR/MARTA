
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound, AnsibleParserError

def test_invalid_input_error_handling():
    dataloader = DataLoader()
    with pytest.raises(AnsibleFileNotFound):
        dataloader.load_from_file('nonexistent_file.yaml')
