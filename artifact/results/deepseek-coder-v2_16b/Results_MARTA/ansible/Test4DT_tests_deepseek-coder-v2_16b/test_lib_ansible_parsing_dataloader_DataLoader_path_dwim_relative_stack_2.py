
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound
import os

def test_path_dwim_relative_stack_with_valid_source():
    dl = DataLoader()
    paths = ['/roles/myrole/tasks', '/playbooks']
    dirname = 'tasks'
    source = 'task.yml'
    with pytest.raises(AnsibleFileNotFound):
        result = dl.path_dwim_relative_stack(paths, dirname, source)
