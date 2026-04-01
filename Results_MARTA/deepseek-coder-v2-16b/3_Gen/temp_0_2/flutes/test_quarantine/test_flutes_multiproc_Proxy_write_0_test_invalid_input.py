
import pytest
from multiprocessing import Queue
from flutes.multiproc import Proxy, Event

@pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        proxy = Proxy(queue=invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy_write_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_Proxy_write_0_test_invalid_input.py:4:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""