
import pytest
from unittest.mock import patch
from pytutils.mappings import ProxyMutableAttrDict

@pytest.mark.parametrize("invalid_input", [
    None,  # None type
    123,   # int type
    "string",  # str type
    [1, 2, 3],  # list type
    (1, 2, 3),  # tuple type
    {1: 'a', 2: 'b'},  # dict-like type
])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        ProxyMutableAttrDict(invalid_input)

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_invalid_inputs.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_invalid_inputs.py:4: in <module>
    from pytutils.mappings import ProxyMutableAttrDict
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_invalid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""