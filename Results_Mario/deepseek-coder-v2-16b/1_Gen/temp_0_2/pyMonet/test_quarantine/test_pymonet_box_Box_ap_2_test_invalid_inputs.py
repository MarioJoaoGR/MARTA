
import pytest
from pymonet.box import Box

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case 1: Passing a non-function type to ap method
        box = Box(lambda x: x + 1)
        result = box.ap("not a function")

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

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            # Test case 1: Passing a non-function type to ap method
            box = Box(lambda x: x + 1)
>           result = box.ap("not a function")

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_2_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.box.Box object at 0x7f016bdf8710>
applicative = 'not a function'

    def ap(self, applicative):
        """
        Applies the function inside the Box[A] structure to another applicative type.
    
        :param applicative: applicative contains function
        :type applicative: Box[B]
        :returns: new Box with result of contains function
        :rtype: Box[A(B)]
        """
>       return applicative.map(self.value)
E       AttributeError: 'str' object has no attribute 'map'

pyMonet/pymonet/box.py:57: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.06s ===============================
"""