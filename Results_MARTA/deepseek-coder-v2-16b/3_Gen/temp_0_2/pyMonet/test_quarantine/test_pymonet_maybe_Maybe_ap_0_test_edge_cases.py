
import pytest
from pymonet.maybe import Maybe

def test_edge_cases():
    # Test None value
    maybe_none = Maybe(value=None, is_nothing=False)
    assert not maybe_none.is_nothing
    assert maybe_none.value is None
    
    # Test empty list
    maybe_empty_list = Maybe(value=[], is_nothing=False)
    assert not maybe_empty_list.is_nothing
    assert maybe_empty_list.value == []
    
    # Test boundary values
    maybe_zero = Maybe(value=0, is_nothing=False)
    assert not maybe_zero.is_nothing
    assert maybe_zero.value == 0
    
    maybe_one = Maybe(value=1, is_nothing=False)
    assert not maybe_one.is_nothing
    assert maybe_one.value == 1
    
    # Test empty Maybe (Nothing)
    maybe_nothing = Maybe(value=None, is_nothing=True)
    assert maybe_nothing.is_nothing
    assert maybe_nothing.value is None
    
    # Test ap method with non-empty Maybe
    def add_one(x):
        return x + 1
    
    maybe_some = Maybe(value=5, is_nothing=False)
    result = maybe_some.ap(Maybe(value=add_one, is_nothing=False))
    assert not result.is_nothing
    assert result.value == 6
    
    # Test ap method with empty Maybe
    result_empty = maybe_none.ap(Maybe(value=add_one, is_nothing=False))
    assert result_empty.is_nothing
    assert result_empty.value is None

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None value
        maybe_none = Maybe(value=None, is_nothing=False)
        assert not maybe_none.is_nothing
        assert maybe_none.value is None
    
        # Test empty list
        maybe_empty_list = Maybe(value=[], is_nothing=False)
        assert not maybe_empty_list.is_nothing
        assert maybe_empty_list.value == []
    
        # Test boundary values
        maybe_zero = Maybe(value=0, is_nothing=False)
        assert not maybe_zero.is_nothing
        assert maybe_zero.value == 0
    
        maybe_one = Maybe(value=1, is_nothing=False)
        assert not maybe_one.is_nothing
        assert maybe_one.value == 1
    
        # Test empty Maybe (Nothing)
        maybe_nothing = Maybe(value=None, is_nothing=True)
        assert maybe_nothing.is_nothing
>       assert maybe_nothing.value is None
E       AttributeError: 'Maybe' object has no attribute 'value'

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_0_test_edge_cases.py:28: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_ap_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.09s ===============================
"""