
import pytest
from pymonet.either import Either, Left, Right

def test_invalid_inputs():
    # Test invalid inputs to check error handling
    left_value = Either(Left("error message"))
    right_value = Either(Right(42))
    
    with pytest.raises(TypeError):
        result = left_value.ap(left_value)  # Should raise TypeError because the function is not applicable to the value in Left
        
    with pytest.raises(TypeError):
        result = right_value.ap(right_function := Either(lambda x: x + 1))  # Should raise TypeError because the function is not applicable to the value in Right

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
        # Test invalid inputs to check error handling
        left_value = Either(Left("error message"))
        right_value = Either(Right(42))
    
        with pytest.raises(TypeError):
>           result = left_value.ap(left_value)  # Should raise TypeError because the function is not applicable to the value in Left

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_invalid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.either.Either object at 0x7fdc1576ba90>
applicative = <pymonet.either.Either object at 0x7fdc1576ba90>

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
============================== 1 failed in 0.08s ===============================
"""