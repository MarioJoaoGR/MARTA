
from unittest.mock import patch, MagicMock
import pytest
import logging
from flutes.log import MultiprocessingFileHandler

@patch('flutes.log.mp')  # Mock the multiprocessing module
def test_send_valid_input(mock_mp):
    mock_queue = MagicMock()
    mock_mp.Queue.return_value = mock_queue
    
    setup_handler = MultiprocessingFileHandler('dummy_path', 'a')  # Create an instance of the handler with a dummy path
    
    log_message = "This is a valid log message"
    
    # Call the send method with the log message
    setup_handler.send(log_message)
    
    # Assert that the queue received the log message
    mock_queue.put_nowait.assert_called_once_with(log_message)
