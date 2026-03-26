
import pytest
from pymonet.semigroups import Min

def test_error_case():
    min1 = Min(3.0)
    invalid_semigroup = 'not a Min instance'
    
    with pytest.raises(TypeError):
        result = min1.concat(invalid_semigroup)

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Min_concat_2_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        min1 = Min(3.0)
        invalid_semigroup = 'not a Min instance'
    
        with pytest.raises(TypeError):
>           result = min1.concat(invalid_semigroup)

pyMonet/Test4DT_tests/test_pymonet_semigroups_Min_concat_2_test_error_case.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.semigroups.Min object at 0x7f3dfe971d10>
semigroup = 'not a Min instance'

    def concat(self, semigroup):
        """
        :param semigroup: other semigroup to concat
        :type semigroup: Min[B]
        :returns: new Min with smallest value
        :rtype: Min[A | B]
        """
>       return Min(self.value if self.value <= semigroup.value else semigroup.value)
E       AttributeError: 'str' object has no attribute 'value'

pyMonet/pymonet/semigroups.py:177: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Min_concat_2_test_error_case.py::test_error_case
============================== 1 failed in 0.07s ===============================
"""