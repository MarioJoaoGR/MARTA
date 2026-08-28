
import pytest
from unittest.mock import patch
from ansible.modules.apt_repository import SourcesList
import os
import tempfile

@pytest.fixture(scope="module")
def sourcelist():
    # Create a temporary directory for the sources list files
    with tempfile.TemporaryDirectory() as tmpdir:
        yield SourcesList(module=None, default_file=os.path.join(tmpdir, 'sources.list'))

# Test valid input scenario
def test_valid_input(sourcelist):
    sourcelist.add_source('deb http://example.com/ubuntu focal main')
    assert len(sourcelist.files) == 1
    assert 'focal' in sourcelist.files

# Test edge case scenario with None value
def test_edge_case():
    with pytest.raises(TypeError):
        SourcesList(module=None, default_file=None).add_source(None)

# Test invalid input scenario
@patch('os.path.isfile', return_value=False)
@patch('glob.iglob', return_value=[''])
def test_invalid_input(_mock_isfile, _mock_iglob):
    with pytest.raises(FileNotFoundError):
        sourcelist = SourcesList(module=None)
        sourcelist.load('/path/to/source/file.list')
