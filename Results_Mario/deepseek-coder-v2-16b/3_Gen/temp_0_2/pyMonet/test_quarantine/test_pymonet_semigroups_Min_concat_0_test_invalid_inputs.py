
import pytest
from pymonet.semigroups import Min

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test invalid input types, e.g., passing a string instead of an instance of Min
        min_monoid = Min(5)
        another_min = "not an instance"  # Invalid input type
        combined_min = min_monoid.concat(another_min)  # This should raise a TypeError

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Min_concat_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            # Test invalid input types, e.g., passing a string instead of an instance of Min
            min_monoid = Min(5)
            another_min = "not an instance"  # Invalid input type
>           combined_min = min_monoid.concat(another_min)  # This should raise a TypeError

pyMonet/Test4DT_tests/test_pymonet_semigroups_Min_concat_0_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.semigroups.Min object at 0x7ff5d11bf4d0>
semigroup = 'not an instance'

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
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Min_concat_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.08s ===============================
"""