
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound, AnsibleParserError


def test_load_data_from_file():
    dl = DataLoader()
    with pytest.raises(AnsibleFileNotFound):
        parsed_data = dl.load_from_file('nonexistent_file')
