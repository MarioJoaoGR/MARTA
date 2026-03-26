
from pymonet.maybe import Maybe
import pytest

def test_invalid_inputs():
    # Test with None value and is_nothing set to True
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing == True
    
    # Test with a valid value and is_nothing set to False
    maybe_some = Maybe(value=42, is_nothing=False)
    assert maybe_some.is_nothing == False
    assert maybe_some.value == 42
    
    # Test with an invalid type for value (should raise a TypeError)
    with pytest.raises(TypeError):
        Maybe(value="invalid", is_nothing=False)
    
    # Test with an invalid type for is_nothing (should raise a TypeError)
    with pytest.raises(TypeError):
        Maybe(value=42, is_nothing="True")

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_lazy_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with None value and is_nothing set to True
        maybe_none = Maybe(value=None, is_nothing=True)
        assert maybe_none.is_nothing == True
    
        # Test with a valid value and is_nothing set to False
        maybe_some = Maybe(value=42, is_nothing=False)
        assert maybe_some.is_nothing == False
        assert maybe_some.value == 42
    
        # Test with an invalid type for value (should raise a TypeError)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_lazy_0_test_invalid_inputs.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_lazy_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.08s ===============================
"""