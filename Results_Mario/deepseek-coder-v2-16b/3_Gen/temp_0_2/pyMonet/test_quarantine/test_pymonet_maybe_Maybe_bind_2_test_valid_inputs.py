
import pytest
from pymonet.maybe import Maybe

def test_valid_inputs():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

    # Test bind method with a valid mapper function
    def double_mapper(x):
        return Maybe(value=x * 2, is_nothing=False)

    result = maybe_some.bind(double_mapper)
    assert not result.is_nothing
    assert result.value == 84

    # Test bind method with a Nothing case
    nothing = Maybe.nothing()
    result_with_nothing = nothing.bind(double_mapper)
    assert result_with_nothing.is_nothing
    assert result_with_nothing.value is None

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_bind_2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        maybe_some = Maybe(value=42, is_nothing=False)
        assert not maybe_some.is_nothing
        assert maybe_some.value == 42
    
        # Test bind method with a valid mapper function
        def double_mapper(x):
            return Maybe(value=x * 2, is_nothing=False)
    
        result = maybe_some.bind(double_mapper)
        assert not result.is_nothing
        assert result.value == 84
    
        # Test bind method with a Nothing case
        nothing = Maybe.nothing()
        result_with_nothing = nothing.bind(double_mapper)
        assert result_with_nothing.is_nothing
>       assert result_with_nothing.value is None
E       AttributeError: 'Maybe' object has no attribute 'value'

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_bind_2_test_valid_inputs.py:22: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_bind_2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""