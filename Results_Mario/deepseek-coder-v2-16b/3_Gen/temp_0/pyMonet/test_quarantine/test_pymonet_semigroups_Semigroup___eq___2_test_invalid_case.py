
import pytest
from pymonet.semigroups import Semigroup

def test_invalid_case():
    s1 = Semigroup(5)
    s2 = 'not a Semigroup'
    with pytest.raises(TypeError):
        assert s1 == s2

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup___eq___2_test_invalid_case.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_case _______________________________

    def test_invalid_case():
        s1 = Semigroup(5)
        s2 = 'not a Semigroup'
        with pytest.raises(TypeError):
>           assert s1 == s2

pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup___eq___2_test_invalid_case.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.semigroups.Semigroup object at 0x7f9967986850>
other = 'not a Semigroup'

    def __eq__(self, other) -> bool:
>       return self.value == other.value
E       AttributeError: 'str' object has no attribute 'value'

pyMonet/pymonet/semigroups.py:14: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup___eq___2_test_invalid_case.py::test_invalid_case
============================== 1 failed in 0.07s ===============================
"""