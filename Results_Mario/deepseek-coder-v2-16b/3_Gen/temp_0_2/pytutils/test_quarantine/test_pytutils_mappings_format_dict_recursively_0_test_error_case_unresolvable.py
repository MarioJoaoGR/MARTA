
import pytest
from pytutils.mappings import format_dict_recursively

def test_error_case_unresolvable():
    c = dict(wat='wat{omg}', omg=True, fail='no{whale}')
    with pytest.raises(ValueError) as excinfo:
        format_dict_recursively(c)
    assert str(excinfo.value) == "Impossible to format dict due to missing elements: {'fail': ['whale']}"

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0_test_error_case_unresolvable.py _
pytutils/Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0_test_error_case_unresolvable.py:3: in <module>
    from pytutils.mappings import format_dict_recursively
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0_test_error_case_unresolvable.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""