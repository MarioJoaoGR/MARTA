
# Module: ansible.modules.apt_repository
import pytest
from unittest.mock import patch, mock_open
import os
import glob
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def sourcelist():
    return SourcesList('deb')

def test_init(sourcelist):
    assert sourcelist.module == 'deb'
    assert isinstance(sourcelist.files, dict)
    assert isinstance(sourcelist.new_repos, set)
    assert sourcelist.default_file == sourcelist._apt_cfg_file('Dir::Etc::sourcelist')

def test_expand_path(sourcelist):
    with patch('os.path.abspath', return_value='/abs/path'):
        assert sourcelist._expand_path('filename') == '/abs/path/filename'
        assert sourcelist._expand_path('/abs/path/filename') == '/abs/path/filename'

def test_load(sourcelist):
    with patch.object(sourcelist, '_apt_cfg_dir', return_value='/etc/sourceparts'):
        with patch('glob.iglob', return_value=['file1', 'file2']):
            sourcelist.load('/path/to/file')  # Assuming load method is mocked to check its behavior

def test_add_source(sourcelist):
    sourcelist.add_source('deb http://example.com/debian stable main', comment='Example repository')
    assert 'deb http://example.com/debian stable main' in sourcelist.files['Dir::Etc::sourcelist']

def test_modify(sourcelist):
    sourcelist.add_source('deb http://example.com/debian stable main', comment='Example repository')
    sourcelist.modify('Dir::Etc::sourcelist', 1, source='deb http://newdomain.com/debian stable main')
    assert sourcelist.files['Dir::Etc::sourcelist'][0] == 'deb http://newdomain.com/debian stable main'

def test_remove_source(sourcelist):
    sourcelist.add_source('deb http://example.com/debian stable main', comment='Example repository')
    sourcelist.remove_source('deb http://example.com/debian stable main')
    assert 'deb http://example.com/debian stable main' not in sourcelist.files['Dir::Etc::sourcelist']

def test_save(sourcelist):
    with patch.object(sourcelist, '_apt_cfg_dir', return_value='/etc/sourceparts'):
        sourcelist.add_source('deb http://example.com/debian stable main', comment='Example repository')
        with patch('builtins.open', mock_open()) as m:
            sourcelist.save()
            assert m.called
