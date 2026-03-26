
import pytest
from flutes.multiproc import _DummyProxy

def test_valid_input():
    dummy_proxy = _DummyProxy()
    with pytest.raises(NotImplementedError):
        dummy_proxy.write("Hello, this is a test message.")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__DummyProxy_write_0_test_valid_input
flutes/Test4DT_tests/test_flutes_multiproc__DummyProxy_write_0_test_valid_input.py:3:0: E0611: No name '_DummyProxy' in module 'flutes.multiproc' (no-name-in-module)


"""