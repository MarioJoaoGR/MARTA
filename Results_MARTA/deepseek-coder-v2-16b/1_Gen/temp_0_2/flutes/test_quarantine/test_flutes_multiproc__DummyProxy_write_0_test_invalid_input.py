
from flutes.multiproc import _DummyProxy

def test_invalid_input():
    dummy_proxy = _DummyProxy()
    try:
        dummy_proxy.write(123)  # Sending an invalid input type to trigger a TypeError
    except TypeError as e:
        assert str(e) == "__init__() takes exactly 1 argument (0 given)"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__DummyProxy_write_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc__DummyProxy_write_0_test_invalid_input.py:2:0: E0611: No name '_DummyProxy' in module 'flutes.multiproc' (no-name-in-module)


"""