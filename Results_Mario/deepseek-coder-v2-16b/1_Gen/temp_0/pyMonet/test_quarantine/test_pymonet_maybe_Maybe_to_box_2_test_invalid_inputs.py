
import pytest
from pymonet.maybe import Maybe
from pymonet.box import Box

def test_invalid_inputs():
    # Test creating Maybe with None value when is_nothing is True
    maybe_none = Maybe(value=None, is_nothing=True)
    assert isinstance(maybe_none.to_box(), Box)
    assert maybe_none.to_box().value is None

    # Test creating Maybe with a value when is_nothing is False
    maybe_value = Maybe(value="Hello", is_nothing=False)
    assert isinstance(maybe_value.to_box(), Box)
    assert maybe_value.to_box().value == "Hello"

    # Test creating Maybe with invalid types for value and is_nothing
    with pytest.raises(TypeError):
        Maybe(value="Hello", is_nothing=1)  # is_nothing should be a bool

    with pytest.raises(TypeError):
        Maybe(value=42, is_nothing="True")  # value should not have a type restriction for None

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

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_box_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test creating Maybe with None value when is_nothing is True
        maybe_none = Maybe(value=None, is_nothing=True)
        assert isinstance(maybe_none.to_box(), Box)
        assert maybe_none.to_box().value is None
    
        # Test creating Maybe with a value when is_nothing is False
        maybe_value = Maybe(value="Hello", is_nothing=False)
        assert isinstance(maybe_value.to_box(), Box)
        assert maybe_value.to_box().value == "Hello"
    
        # Test creating Maybe with invalid types for value and is_nothing
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_box_2_test_invalid_inputs.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_box_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.07s ===============================
"""