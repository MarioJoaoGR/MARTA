
import pytest
from pymonet.maybe import Maybe

def test_invalid_inputs():
    # Test invalid inputs for the ap method
    
    # Create an instance of Maybe with a value and another instance with nothing
    maybe_some = Maybe(value=42, is_nothing=False)
    maybe_none = Maybe(value=None, is_nothing=True)
    
    # Test applying to a valid Maybe
    result = maybe_some.ap(Maybe(value=lambda x: x + 1, is_nothing=False))
    
    # Assert that the result is not nothing and has the expected value
    assert not result.is_nothing
    assert result.value == 43

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test invalid inputs for the ap method
    
        # Create an instance of Maybe with a value and another instance with nothing
        maybe_some = Maybe(value=42, is_nothing=False)
        maybe_none = Maybe(value=None, is_nothing=True)
    
        # Test applying to a valid Maybe
>       result = maybe_some.ap(Maybe(value=lambda x: x + 1, is_nothing=False))

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_2_test_invalid_inputs.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/maybe.py:85: in ap
    return applicative.map(self.value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.maybe.Maybe object at 0x7f5d611bcc90>, mapper = 42

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
E       TypeError: 'int' object is not callable

pyMonet/pymonet/maybe.py:57: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.11s ===============================
"""