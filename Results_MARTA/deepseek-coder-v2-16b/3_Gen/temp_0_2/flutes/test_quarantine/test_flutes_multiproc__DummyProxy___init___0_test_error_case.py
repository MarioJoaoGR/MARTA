
from flutes.multiproc import _DummyProxy

def test_error_case():
    assert isinstance(_DummyProxy(), _DummyProxy)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__DummyProxy___init___0_test_error_case
flutes/Test4DT_tests/test_flutes_multiproc__DummyProxy___init___0_test_error_case.py:2:0: E0611: No name '_DummyProxy' in module 'flutes.multiproc' (no-name-in-module)


"""