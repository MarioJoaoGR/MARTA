
import pytest
from collections import OrderedDict
from pytutils.mappings import PrefixedProxyMutableMapping

@pytest.fixture
def prefixed_mapping():
    my_dict = {'foo': 1, 'bar': 2}
    return PrefixedProxyMutableMapping('pre_', my_dict)

def test_access_key_with_prefix(prefixed_mapping):
    assert prefixed_mapping['pre_foo'] == 1

def test_add_new_key_with_prefix(prefixed_mapping):
    prefixed_mapping['new_key'] = 3
    assert 'new_key' in prefixed_mapping
    assert prefixed_mapping['pre_new_key'] == 3

def test_remove_key_with_prefix(prefixed_mapping):
    del prefixed_mapping['pre_foo']
    with pytest.raises(KeyError):
        prefixed_mapping['pre_foo']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""