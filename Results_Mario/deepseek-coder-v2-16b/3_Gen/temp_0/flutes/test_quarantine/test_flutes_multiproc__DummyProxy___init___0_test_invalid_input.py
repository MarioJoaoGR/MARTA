
from flutes.multiproc import _DummyProxy
import pytest

def test_invalid_input():
    with pytest.raises(TypeError):
        dummy_proxy = _DummyProxy()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__DummyProxy___init___0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc__DummyProxy___init___0_test_invalid_input.py:2:0: E0611: No name '_DummyProxy' in module 'flutes.multiproc' (no-name-in-module)


"""