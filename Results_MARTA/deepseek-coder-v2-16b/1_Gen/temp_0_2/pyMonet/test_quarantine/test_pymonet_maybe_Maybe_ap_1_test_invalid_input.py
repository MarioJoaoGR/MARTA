
import pytest
from pymonet.maybe import Maybe

def test_invalid_input():
    maybe_invalid = Maybe(value='invalid', is_nothing=False)
    applicative_invalid = 'invalid'
    
    # Test ap method with invalid input
    result = maybe_invalid.ap(applicative_invalid)
    
    assert isinstance(result, Maybe)
    assert result.is_nothing

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        maybe_invalid = Maybe(value='invalid', is_nothing=False)
        applicative_invalid = 'invalid'
    
        # Test ap method with invalid input
>       result = maybe_invalid.ap(applicative_invalid)

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_1_test_invalid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.maybe.Maybe object at 0x7fc1175d73d0>, applicative = 'invalid'

    def ap(self, applicative):
        """
        Applies the function inside the Maybe[A] structure to another applicative type for notempty Maybe.
        For empty returns copy of itself
    
        :param applicative: applicative contains function
        :type applicative: Maybe[B]
        :returns: new Maybe with result of contains function
        :rtype: Maybe[A(B) | None]
        """
        if self.is_nothing:
            return Maybe.nothing()
>       return applicative.map(self.value)
E       AttributeError: 'str' object has no attribute 'map'

pyMonet/pymonet/maybe.py:85: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""