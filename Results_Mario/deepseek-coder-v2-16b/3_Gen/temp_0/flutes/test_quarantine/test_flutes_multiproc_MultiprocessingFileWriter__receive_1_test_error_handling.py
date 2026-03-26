
import pytest
from flutes.multiproc import MultiprocessingFileWriter
import multiprocessing as mp
import threading
from unittest.mock import MagicMock, patch

@pytest.fixture(scope="function")
def setup_writer():
    path = "testfile.log"
    writer = MultiprocessingFileWriter(path)
    yield writer
    # Teardown: Close the file and join the thread if necessary
    writer._thread.join()
    writer._file.close()

@pytest.mark.parametrize("eof_error", [EOFError])
def test_error_handling(setup_writer, eof_error):
    with patch('builtins.open', create=True) as mock_open:
        mock_queue = mp.Queue()
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        
        # Set up the writer with a mocked queue that raises EOFError after one record
        setup_writer._queue = mock_queue
        mock_queue.get.side_effect = [MagicMock(), EOFError]
        
        # Start the receive process
        setup_writer._receive()
        
        # Check if the file was written correctly until EOFError is encountered
        assert mock_file.write.call_count == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""