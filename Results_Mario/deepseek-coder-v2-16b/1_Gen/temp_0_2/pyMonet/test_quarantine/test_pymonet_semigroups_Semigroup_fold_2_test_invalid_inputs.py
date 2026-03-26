
import pytest
from pymonet.semigroups import Semigroup

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test that passing an invalid type to the constructor raises a TypeError
        s = Semigroup(5)  # Passing an integer, which should be fine as per current implementation
        
        # Now pass an invalid type, such as a string, which should raise a TypeError
        with pytest.raises(TypeError):
            Semigroup("hello")

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup_fold_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            # Test that passing an invalid type to the constructor raises a TypeError
            s = Semigroup(5)  # Passing an integer, which should be fine as per current implementation
    
            # Now pass an invalid type, such as a string, which should raise a TypeError
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup_fold_2_test_invalid_inputs.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup_fold_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.06s ===============================
"""