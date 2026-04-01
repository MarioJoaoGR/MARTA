
import pytest
from pymonet.semigroups import One

def test_invalid_input_none():
    """
    Test that concat method raises a TypeError when given None as an argument.
    """
    one = One(False)  # Instantiating with False
    
    with pytest.raises(TypeError):
        one.concat(None)  # Attempting to concatenate with None should raise a TypeError

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_1_test_invalid_input_none.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_none ____________________________

    def test_invalid_input_none():
        """
        Test that concat method raises a TypeError when given None as an argument.
        """
        one = One(False)  # Instantiating with False
    
        with pytest.raises(TypeError):
>           one.concat(None)  # Attempting to concatenate with None should raise a TypeError

pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_1_test_invalid_input_none.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.semigroups.One object at 0x7f29f6f4f590>, semigroup = None

    def concat(self, semigroup):
        """
        :param semigroup: other semigroup to concat
        :type semigroup: One[B]
        :returns: new One with first truly value or last falsy
        :rtype: One[A | B]
        """
>       return One(self.value or semigroup.value)
E       AttributeError: 'NoneType' object has no attribute 'value'

pyMonet/pymonet/semigroups.py:81: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_1_test_invalid_input_none.py::test_invalid_input_none
============================== 1 failed in 0.09s ===============================
"""