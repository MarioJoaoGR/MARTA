
from pymonet.either import Either, Left, Right
import pytest

def test_invalid_inputs():
    # Test with invalid input types
    left_value = Either(Left("error message"))
    right_function = Either(Right(lambda x: x + 1))
    
    with pytest.raises(TypeError):
        result = left_value.ap(right_function)

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with invalid input types
        left_value = Either(Left("error message"))
        right_function = Either(Right(lambda x: x + 1))
    
        with pytest.raises(TypeError):
>           result = left_value.ap(right_function)

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_invalid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.either.Either object at 0x7fefff9f7a90>
applicative = <pymonet.either.Either object at 0x7ff000b5f450>

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
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.10s ===============================
"""