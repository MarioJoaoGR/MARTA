
from pymonet.either import Either, Left, Right

def test_ap():
    # Test case for Left containing a function and Right with a value
    left_function = Either(Left(lambda x: x + 1))
    right_value = Either(Right(5))
    result = left_function.ap(right_value)
    assert result.value == 6

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________________ test_ap ____________________________________

    def test_ap():
        # Test case for Left containing a function and Right with a value
        left_function = Either(Left(lambda x: x + 1))
        right_value = Either(Right(5))
>       result = left_function.ap(right_value)

pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_edge_cases.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.either.Either object at 0x7ff0390dd690>
applicative = <pymonet.either.Either object at 0x7ff038c35f10>

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
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_ap_0_test_edge_cases.py::test_ap
============================== 1 failed in 0.08s ===============================
"""