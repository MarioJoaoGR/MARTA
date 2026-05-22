
import sys
import threading
from unittest.mock import patch, MagicMock
import httpie.uploads as uploads

def test_none_input():
    env = MagicMock()
    file = MagicMock()
    read_event = threading.Event()

    with patch('httpie.uploads.is_windows', return_value=False):
        with patch('httpie.uploads.READ_THRESHOLD', 10):
            uploads.observe_stdin_for_data_thread(env, file, read_event)

            # Wait for the thread to complete (or timeout)
            threading.Event().wait(timeout=15)

            assert env.stderr.write.call_count == 0
