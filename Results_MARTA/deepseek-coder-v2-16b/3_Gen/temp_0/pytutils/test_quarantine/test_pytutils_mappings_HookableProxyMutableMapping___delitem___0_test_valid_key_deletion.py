
import pytest
from unittest.mock import MagicMock
from pytutils.mappings import HookableProxyMutableMapping

def test_valid_key_deletion():
    # Create a mock dictionary-like object
    mapping = MagicMock()
    
    # Instantiate the HookableProxyMutableMapping with the mock mapping
    proxy_map = HookableProxyMutableMapping(mapping)
    
    # Define a key to be deleted
    key_to_delete = 'key1'
    
    # Set up the mock to expect a call to delete the key
    mapping.__delitem__.side_effect = lambda item: print(f"Deleting {item}")
    
    # Call the __delitem__ method of the proxy map
    del proxy_map[key_to_delete]
    
    # Assert that the mock's __delitem__ method was called with the correct key
    mapping.__delitem__.assert_called_with(key_to_delete)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""