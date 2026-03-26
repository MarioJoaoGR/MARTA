
# Module: pytutils.mappings
from pytutils.mappings import ProxyMutableMapping
import pytest

@pytest.fixture
def example_dict():
    return {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}

@pytest.fixture
def proxy_mapping(example_dict):
    return ProxyMutableMapping(example_dict)

# Test cases for __init__ method
def test_init_with_default_params():
    a = {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}
    b = ProxyMutableMapping(a)
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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___setitem___0.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___setitem___0.py:3: in <module>
    from pytutils.mappings import ProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___setitem___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""