
import pytest
from ansible.modules.yum_repository import YumRepo
import os
import configparser

@pytest.fixture(scope="module")
def get_full_module():
    class FullModule:
        def __init__(self):
            self.params = {
                'repoid': 'test_repo',
                'reposdir': '/tmp/test_repo_dir',
                'file': 'test_repo_file'
            }
    
    return FullModule

@pytest.fixture(scope="module")
def get_invalid_module():
    class InvalidModule:
        def __init__(self):
            self.params = {
                'repoid': 'test_repo',
                'reposdir': '',  # Invalid directory
                'file': 'test_repo_file'
            }
    
    return InvalidModule



def test_invalid_input(get_invalid_module):
    module = get_invalid_module()
    with pytest.raises(Exception):
        repo = YumRepo(module)