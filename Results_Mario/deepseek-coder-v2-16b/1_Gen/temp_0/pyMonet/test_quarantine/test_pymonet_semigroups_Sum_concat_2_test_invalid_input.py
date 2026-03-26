
import pytest
from pymonet.semigroups import Sum

def test_invalid_input():
    # Create an instance of Sum with a valid integer value
    sum1 = Sum(3)
    
    # Try to concatenate with a non-Sum object (e.g., an integer)
    with pytest.raises(TypeError):
        result = sum1.concat(5)  # This should raise TypeError because 5 is not an instance of Sum

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Sum_concat_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Create an instance of Sum with a valid integer value
        sum1 = Sum(3)
    
        # Try to concatenate with a non-Sum object (e.g., an integer)
        with pytest.raises(TypeError):
>           result = sum1.concat(5)  # This should raise TypeError because 5 is not an instance of Sum

pyMonet/Test4DT_tests/test_pymonet_semigroups_Sum_concat_2_test_invalid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.semigroups.Sum object at 0x7fde2336e2d0>, semigroup = 5

    def concat(self, semigroup: 'Sum') -> 'Sum':
        """
        :param semigroup: other semigroup to concat
        :type semigroup: Sum[B]
        :returns: new Sum with sum of concat semigroups values
        :rtype: Sum[A]
        """
>       return Sum(self.value + semigroup.value)
E       AttributeError: 'int' object has no attribute 'value'

pyMonet/pymonet/semigroups.py:41: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Sum_concat_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""