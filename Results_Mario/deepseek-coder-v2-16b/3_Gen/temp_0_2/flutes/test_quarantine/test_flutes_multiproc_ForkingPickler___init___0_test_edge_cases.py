
import pytest
from flutes.multiproc import ForkingPickler
import pickle

@pytest.mark.parametrize("args, kwargs", [
    ((), {"protocol": pickle.HIGHEST_PROTOCOL}),
    ((None,), {"protocol": pickle.HIGHEST_PROTOCOL}),
    ((None, None), {"protocol": pickle.HIGHEST_PROTOCOL})
])
def test_ForkingPickler_init(args, kwargs):
    pickler = ForkingPickler(*args, **kwargs)
    assert isinstance(pickler, ForkingPickler)
    if len(args) >= 2:
        assert args[0] is None or isinstance(args[0], str)
    else:
        assert kwargs["protocol"] == pickle.HIGHEST_PROTOCOL

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ForkingPickler___init___0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_ForkingPickler___init___0_test_edge_cases.py:3:0: E0611: No name 'ForkingPickler' in module 'flutes.multiproc' (no-name-in-module)


"""