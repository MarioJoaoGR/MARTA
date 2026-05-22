
import sys
import threading
from unittest.mock import patch, MagicMock
from httpie.uploads import Environment, observe_stdin_for_data_thread

def test_invalid_input():
    env = Environment()
    read_event = threading.Event()
    
    # Mock the environment to capture stderr output
    with patch('sys.stderr', new=MagicMock()) as mock_stderr:
        observe_stdin_for_data_thread(env, sys.stdin, read_event)
        
        # Wait for a short period to ensure the thread has started
        threading.Event().wait(timeout=0.1)
        
        # Check that no warning was issued (since stdin is not being mocked)
        assert mock_stderr.write.call_count == 0
