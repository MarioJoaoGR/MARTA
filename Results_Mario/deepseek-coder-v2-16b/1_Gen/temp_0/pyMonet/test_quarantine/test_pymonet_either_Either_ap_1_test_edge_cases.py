
import pytest
from pymonet.either import Either, Left, Right

def test_ap():
    # Test case for Left with a function and Right value
    left_function = Either(Left("error message"))  # A Left containing a lambda function
    right_value = Either(Right(5))  # Creates a Right with value 5
    
    # Applies the function inside the Left structure to the Right instance
    result = left_function.ap(right_value)
    
    assert str(result) == "Left('error message')"

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________________ test_ap ____________________________________

    def test_ap():
        # Test case for Left with a function and Right value
        left_function = Either(Left("error message"))  # A Left containing a lambda function
        right_value = Either(Right(5))  # Creates a Right with value 5
    
        # Applies the function inside the Left structure to the Right instance
>       result = left_function.ap(right_value)

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_1_test_edge_cases.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.either.Either object at 0x7f67f334a850>
applicative = <pymonet.either.Either object at 0x7f67f3348190>

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
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_1_test_edge_cases.py::test_ap
============================== 1 failed in 0.07s ===============================
"""