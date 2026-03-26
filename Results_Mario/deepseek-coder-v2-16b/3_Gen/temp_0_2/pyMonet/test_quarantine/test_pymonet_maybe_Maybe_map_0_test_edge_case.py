
import pytest
from pymonet.maybe import Maybe

def test_edge_case():
    # Test when value is None and is_nothing is True
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing is True
    assert maybe_none.map(lambda x: x * 2) == Maybe.nothing()
    
    # Test when value is not None and is_nothing is False
    maybe_some = Maybe(value=42, is_nothing=False)
    assert maybe_some.is_nothing is False
    assert maybe_some.map(lambda x: x * 2).value == 84
    
    # Test when value is None and is_nothing is False (should not happen as per class definition)
    with pytest.raises(AttributeError):
        Maybe(value=None, is_nothing=False)

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_map_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Test when value is None and is_nothing is True
        maybe_none = Maybe(value=None, is_nothing=True)
        assert maybe_none.is_nothing is True
        assert maybe_none.map(lambda x: x * 2) == Maybe.nothing()
    
        # Test when value is not None and is_nothing is False
        maybe_some = Maybe(value=42, is_nothing=False)
        assert maybe_some.is_nothing is False
        assert maybe_some.map(lambda x: x * 2).value == 84
    
        # Test when value is None and is_nothing is False (should not happen as per class definition)
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_map_0_test_edge_case.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_map_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.08s ===============================
"""