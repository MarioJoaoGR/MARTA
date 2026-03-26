
import pytest
from pymonet.validation import Validation
from pymonet.monad_try import Try

def test_edge_case_none():
    # Test when errors is None (should be treated as an empty list)
    val = Validation("Success", None)
    try_val = val.to_try()
    
    assert try_val.is_success(), "Expected success, but got failure"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_try_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        # Test when errors is None (should be treated as an empty list)
        val = Validation("Success", None)
>       try_val = val.to_try()

pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_try_0_test_edge_case_none.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/validation.py:155: in to_try
    return Try(self.value, is_success=self.is_success())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.validation.Validation object at 0x7f54f1fd0f10>

    def is_success(self):
        """
        Returns True when errors list are empty.
    
        :returns: True for empty errors list
        :rtype: Boolean
        """
>       return len(self.errors) == 0
E       TypeError: object of type 'NoneType' has no len()

pyMonet/pymonet/validation.py:52: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_validation_Validation_to_try_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.08s ===============================
"""