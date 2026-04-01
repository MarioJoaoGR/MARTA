
import pytest
from pymonet.maybe import Maybe

def test_edge_case():
    # Setup
    maybe_none = Maybe(value=None, is_nothing=False)
    applicative_empty = Maybe(value=lambda x: x + 1, is_nothing=True)
    
    # Test when self is not empty and applicative is not empty
    result = maybe_none.ap(Maybe(value=lambda y: y * 2, is_nothing=False))
    
    # Assert the expected behavior
    assert result.is_nothing == True

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_1_test_edge_case.py F  [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Setup
        maybe_none = Maybe(value=None, is_nothing=False)
        applicative_empty = Maybe(value=lambda x: x + 1, is_nothing=True)
    
        # Test when self is not empty and applicative is not empty
>       result = maybe_none.ap(Maybe(value=lambda y: y * 2, is_nothing=False))

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_1_test_edge_case.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/maybe.py:85: in ap
    return applicative.map(self.value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.maybe.Maybe object at 0x7ff78b4ed490>, mapper = None

    def map(self, mapper: Callable[[T], U]) -> Union['Maybe[U]', 'Maybe[None]']:
        """
        If Maybe is empty return new empty Maybe, in other case
        takes mapper function and returns new instance of Maybe
        with result of mapper.
    
        :param mapper: function to call with Maybe value
        :type mapper: Function(A) -> B
        :returns: Maybe[B | None]
        """
        if self.is_nothing:
            return Maybe.nothing()
        return Maybe.just(
>           mapper(self.value)
        )
E       TypeError: 'NoneType' object is not callable

pyMonet/pymonet/maybe.py:57: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.07s ===============================
"""