
import pytest
from pytutils.mappings import format_dict_recursively

def test_valid_input():
    c = dict(wat='wat{omg}', omg=True)
    expected = {'omg': True, 'wat': 'watTrue'}
    assert format_dict_recursively(c) == expected

    # Dealing with missing (unresolvable) keys in format strings
    c = dict(wat='wat{omg}', omg=True, fail='no{whale}')
    result = format_dict_recursively(c, raise_unresolvable=False)
    expected = {'fail': 'no{whale}', 'omg': True, 'wat': 'watTrue'}
    assert result == expected

    result = format_dict_recursively(c, raise_unresolvable=False, strip_unresolvable=True)
    expected = {'omg': True, 'wat': 'watTrue'}
    assert result == expected

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0_test_valid_input.py _
pytutils/Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0_test_valid_input.py:3: in <module>
    from pytutils.mappings import format_dict_recursively
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""