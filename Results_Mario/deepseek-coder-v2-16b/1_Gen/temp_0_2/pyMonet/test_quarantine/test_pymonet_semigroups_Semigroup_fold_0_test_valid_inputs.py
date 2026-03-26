
import pytest
from pymonet.semigroups import Semigroup

def test_valid_inputs():
    s = Semigroup(5)
    def add_one(x): return x + 1
    def to_upper(x): return x.upper()
    
    assert s.fold(add_one) == 6
    assert s.fold(to_upper) == "HELLO"

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup_fold_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        s = Semigroup(5)
        def add_one(x): return x + 1
        def to_upper(x): return x.upper()
    
        assert s.fold(add_one) == 6
>       assert s.fold(to_upper) == "HELLO"

pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup_fold_0_test_valid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/semigroups.py:17: in fold
    return fn(self.value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 5

>   def to_upper(x): return x.upper()
E   AttributeError: 'int' object has no attribute 'upper'

pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup_fold_0_test_valid_inputs.py:8: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup_fold_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.05s ===============================
"""