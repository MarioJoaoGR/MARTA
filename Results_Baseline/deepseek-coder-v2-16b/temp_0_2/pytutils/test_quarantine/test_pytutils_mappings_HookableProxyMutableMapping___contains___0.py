
import pytest
from collections import UserDict
from pytutils.mappings import HookableProxyMutableMapping  # Importing from module

# Fixture to create a sample hookable mapping for testing
@pytest.fixture
def sample_mapping():
    return {'key1': 'value1', 'key2': 'value2'}

# Test the basic functionality of the HookableProxyMutableMapping class
def test_basic_functionality(sample_mapping):
    hookable_proxy = HookableProxyMutableMapping(sample_mapping)
    
    # Check initial representation
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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___contains___0.py _
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___contains___0.py:4: in <module>
    from pytutils.mappings import HookableProxyMutableMapping  # Importing from module
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___contains___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""