
import pytest
from ansible.playbook import PlaybookInclude
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound

def test_valid_inputs():
    playbook_include = PlaybookInclude()
    ds = {'import_playbook': 'example_playbook.yml'}
    basedir = '/path/to/basedir'
    loader = DataLoader()
    
    with pytest.raises(AnsibleFileNotFound):
        new_playbook = playbook_include.load_data(ds, basedir, loader=loader)

def test_invalid_inputs():
    playbook_include = PlaybookInclude()
    ds = {'import_playbook': 'nonexistent_playbook.yml'}
    basedir = '/path/to/basedir'
    loader = DataLoader()
    
    with pytest.raises(AnsibleFileNotFound):
        new_playbook = playbook_include.load_data(ds, basedir, loader=loader)
