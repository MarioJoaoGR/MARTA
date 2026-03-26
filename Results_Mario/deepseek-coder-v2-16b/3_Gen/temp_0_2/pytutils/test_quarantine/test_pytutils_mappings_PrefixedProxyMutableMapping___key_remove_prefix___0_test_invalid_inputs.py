
import pytest
from pytutils.mappings import PrefixedProxyMutableMapping
from collections import defaultdict, OrderedDict

def test_invalid_inputs():
    with pytest.raises(AttributeError):
        # Test with invalid mapping type (should raise AttributeError)
        PrefixedProxyMutableMapping('pre_', 'not a valid mapping')

    with pytest.raises(TypeError):
        # Test with non-string prefix (should raise TypeError)
        PrefixedProxyMutableMapping(123, defaultdict(int))

    with pytest.raises(ValueError):
        # Test with empty string as prefix (should raise ValueError)
        PrefixedProxyMutableMapping('', OrderedDict([('key', 'value')]))

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_invalid_inputs.py _
pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_invalid_inputs.py:3: in <module>
    from pytutils.mappings import PrefixedProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_invalid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""