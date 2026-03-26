
# Importing the HookableProxyMutableMapping class from pytutils.mappings
from pytutils.mappings import HookableProxyMutableMapping
import pytest

def test_custom_key_allowed():
    # Create a mock mapping for testing
    my_dict = {'a': 1, 'b': 2}
    proxy_map = HookableProxyMutableMapping(my_dict)
    
    # Test the default behavior where all keys are allowed
    assert proxy_map.__key_allowed__('any_key') is True

    # Optionally, you can override the __key_allowed__ method in a subclass and test that specific logic
    class MyHookableMapping(HookableProxyMutableMapping):
        def __key_allowed__(self, key):
            return isinstance(key, int) or key == 'foo'
    
    my_mapping = {'foo': 42}
    hookable_map = MyHookableMapping(my_mapping)
    
    # Test the allowed keys in the subclass
    assert hookable_map.__key_allowed__('foo') is True
    assert hookable_map.__key_allowed__(1) is False  # Since 1 is an int and not 'foo'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_custom_key_allowed.py _
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_custom_key_allowed.py:3: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_custom_key_allowed.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""