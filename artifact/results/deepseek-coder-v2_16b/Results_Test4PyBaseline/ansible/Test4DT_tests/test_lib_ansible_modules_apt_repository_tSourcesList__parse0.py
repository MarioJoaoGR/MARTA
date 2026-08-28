# Module: ansible.modules.apt_repository
import pytest
from your_module import SourcesList
import os
import glob

# Assuming VALID_SOURCE_TYPES is defined somewhere in the module
VALID_SOURCE_TYPES = ['deb']

class InvalidSource(Exception):
    pass

@pytest.fixture
def sourcelist():
    return SourcesList('deb')

def test_init_sourceslist(sourcelist):
    assert sourcelist.module == 'deb'
    assert isinstance(sourcelist.files, dict)
    assert isinstance(sourcelist.new_repos, set)
    assert sourcelist.default_file == sourcelist._apt_cfg_file('Dir::Etc::sourcelist')
    assert os.path.isfile(sourcelist.default_file)
    for file in glob.iglob('%s/*.list' % sourcelist._apt_cfg_dir('Dir::Etc::sourceparts')):
        assert os.path.isfile(file)

def test_parse_valid_line(sourcelist):
    line = 'deb http://example.com/debian stable main'
    valid, enabled, source, comment = sourcelist._parse(line)
    assert valid
    assert enabled
    assert source == 'deb http://example.com/debian stable main'
    assert comment == ''

def test_parse_disabled_line(sourcelist):
    line = '# deb http://example.com/debian stable main'
    valid, enabled, source, comment = sourcelist._parse(line)
    assert not enabled
    assert source == 'deb http://example.com/debian stable main'
    assert comment == ''

def test_parse_invalid_line(sourcelist):
    line = 'invalid source line'
    with pytest.raises(InvalidSource):
        sourcelist._parse(line, raise_if_invalid_or_disabled=True)

def test_parse_commented_line(sourcelist):
    line = '# deb http://example.com/debian stable main # this is a comment'
    valid, enabled, source, comment = sourcelist._parse(line)
    assert not enabled
    assert source == 'deb http://example.com/debian stable main'
    assert comment == 'this is a comment'
