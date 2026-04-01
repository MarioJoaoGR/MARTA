
import pytest
from pymonet.box import Box

def test_invalid_input():
    with pytest.raises(TypeError):
        box = Box('string')  # This should be fine since 'string' is valid input
        applicative = Box(123)  # This should also be fine since 123 is a valid integer

        # Now let's try to apply the function with invalid types
        with pytest.raises(TypeError):
            box.ap('not_a_function')  # This should raise TypeError because 'not_a_function' is not callable

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

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_0_test_invalid_input.py F  [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            box = Box('string')  # This should be fine since 'string' is valid input
            applicative = Box(123)  # This should also be fine since 123 is a valid integer
    
            # Now let's try to apply the function with invalid types
            with pytest.raises(TypeError):
>               box.ap('not_a_function')  # This should raise TypeError because 'not_a_function' is not callable

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_0_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.box.Box object at 0x7f4925823050>
applicative = 'not_a_function'

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
FAILED pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""