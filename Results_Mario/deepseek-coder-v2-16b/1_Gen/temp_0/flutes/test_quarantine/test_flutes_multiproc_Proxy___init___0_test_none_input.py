
import multiprocessing as mp
from flutes.multiproc import Event, Proxy

class TestProxyInit:
    def test_none_input(self):
        # Arrange
        queue = mp.Queue()
        
        # Act
        proxy = Proxy(queue)
        
        # Assert
        assert isinstance(proxy.queue, mp.Queue)
        assert proxy.queue == queue

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy___init___0_test_none_input
flutes/Test4DT_tests/test_flutes_multiproc_Proxy___init___0_test_none_input.py:3:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""