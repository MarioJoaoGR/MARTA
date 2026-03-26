
import pytest
from unittest.mock import MagicMock, patch
from pytutils.mappings import PrefixedProxyMutableMapping

@pytest.fixture
def setup_prefixed_mapping():
    mapping = {'foo': 1, 'bar': 2}
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', mapping)
    return prefixed_mapping

def test_add_new_key(setup_prefixed_mapping):
    setup_prefixed_mapping['new_key'] = 3
    assert 'new_key' in setup_prefixed_mapping
    assert setup_prefixed_mapping['pre_new_key'] == 3

def test_access_existing_key(setup_prefixed_mapping):
    assert setup_prefixed_mapping['pre_foo'] == 1

def test_remove_existing_key(setup_prefixed_mapping):
    del setup_prefixed_mapping['pre_foo']
    with pytest.raises(KeyError):
        setup_prefixed_mapping['pre_foo']

@patch('pytutils.mappings.PrefixedProxyMutableMapping.__init__', lambda x, y, z: None)
def test_custom_init():
    mapping = MagicMock()
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', mapping)
    assert prefixed_mapping._PrefixedProxyMutableMapping__prefix == 'pre_'
    assert prefixed_mapping._PrefixedProxyMutableMapping__only_prefixed is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""