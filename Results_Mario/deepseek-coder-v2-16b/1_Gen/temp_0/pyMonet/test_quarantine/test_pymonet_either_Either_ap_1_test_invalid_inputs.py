
import pytest
from pymonet.either import Either, Left, Right

def test_invalid_inputs():
    # Test with a non-function in the applicative (Left)
    left_value = Either(Left("error message"))
    result1 = left_value.ap(left_value)
    
    assert isinstance(result1, Left), "Expected Left type"
    assert str(result1.value) == "error message", "Expected error message in Left"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with a non-function in the applicative (Left)
        left_value = Either(Left("error message"))
>       result1 = left_value.ap(left_value)

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_1_test_invalid_inputs.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.either.Either object at 0x7efffb7c6590>
applicative = <pymonet.either.Either object at 0x7efffb7c6590>

    def ap(self, applicative):
        """
        Applies the function inside the Either[A] structure to another applicative type.
    
        :param applicative: applicative contains function
        :type applicative: Either[B]
        :returns: new Either with result of contains function
        :rtype: Either[A(B)]
        """
>       return applicative.map(self.value)
E       AttributeError: 'Either' object has no attribute 'map'

pyMonet/pymonet/either.py:46: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.07s ===============================
"""