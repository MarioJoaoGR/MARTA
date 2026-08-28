
# Module: ansible.modules.apt_repository
import pytest
from unittest.mock import patch, MagicMock
import os
import glob
from ansible.modules.apt_repository import SourcesList
from unittest.mock import mock_open

@pytest.fixture
def sourcelist():
    return SourcesList('deb')

def test_init(sourcelist):
    assert sourcelist.module == 'deb'
    assert isinstance(sourcelist.files, dict)
    assert isinstance(sourcelist.new_repos, set)
    assert sourcelist.default_file == sourcelist._apt_cfg_file('Dir::Etc::sourcelist')

@patch('ansible.modules.apt_repository.os.path.isfile', return_value=True)
def test_load(mock_isfile, sourcelist):
    mock_isfile.return_value = True
    with patch('ansible.modules.apt_repository.glob.iglob') as mock_glob:
        mock_glob.return_value = ['file1', 'file2']
        sourcelist.load(sourcelist.default_file)
        assert len(sourcelist.files) == 3  # includes default file and list files

@patch('ansible.modules.apt_repository.os.path.isfile', return_value=False)
def test_load_no_files(mock_isfile, sourcelist):
    mock_isfile.return_value = False
    with patch('ansible.modules.apt_repository.glob.iglob') as mock_glob:
        mock_glob.return_value = []
        sourcelist.load(sourcelist.default_file)
        assert len(sourcelist.files) == 0

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
    sourcelist.add_source('deb http://example.com/debian stable main', comment='Example repository')
    with patch('builtins.open', mock_open()) as mocked_file:
        sourcelist.save()
        assert mocked_file.call_count == 1
