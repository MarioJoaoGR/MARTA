
# Module: ansible.playbook.playbook_include
# test_playbook_include.py
from ansible.playbook import PlaybookInclude
from ansible.errors import AnsibleParserError
import pytest

@pytest.fixture
def playbook_include():
    return PlaybookInclude()

# Test cases for _preprocess_import method

def test_missing_import_playbook(playbook_include):
    with pytest.raises(AnsibleParserError) as excinfo:
        playbook_include._preprocess_import({}, {}, 'import_playbook', None)
    assert "playbook import parameter is missing" in str(excinfo.value)

def test_non_string_import_playbook(playbook_include):
    with pytest.raises(AnsibleParserError) as excinfo:
        playbook_include._preprocess_import({}, {}, 'import_playbook', 123)
    assert "playbook import parameter must be a string indicating a file path, got <class 'int'> instead" in str(excinfo.value)

def test_empty_import_playbook(playbook_include):
    with pytest.raises(AnsibleParserError) as excinfo:
        playbook_include._preprocess_import({}, {}, 'import_playbook', '')
    assert "import_playbook statements must specify the file name to import" in str(excinfo.value)

def test_valid_import_playbook(playbook_include):
    result = playbook_include._preprocess_import({}, {}, 'import_playbook', 'example.yml')