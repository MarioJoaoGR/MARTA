
import pytest
from unittest.mock import MagicMock
import pytutils.queues as queues

def test_invalid_input():
    # Mock broken queue 'q' and output queues 'out_queues'
    q = None  # Assuming a broken queue that does not exist
    out_queues = [MagicMock(), MagicMock()]  # Two mock queues
    
    with pytest.raises(Exception):
        def f():
            while True:
                x = q.get()
                for out_q in out_queues:
                    out_q.put(x)
        
        # Call the function to trigger the exception
        f()
