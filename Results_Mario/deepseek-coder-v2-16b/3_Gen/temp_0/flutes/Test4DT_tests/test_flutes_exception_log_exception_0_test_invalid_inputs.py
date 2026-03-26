
import pytest
from unittest.mock import patch, MagicMock
from flutes.exception import log_exception

def test_log_exception():
    # Mocking an exception
    e = ValueError("Invalid value")
    
    with patch('flutes.exception.log') as mock_log:
        log_exception(e)
        
        # Check if the function was called correctly without user message
        mock_log.assert_called_with(f"<{e.__class__.__qualname__}> {e}", "error")

    with patch('flutes.exception.log') as mock_log:
        log_exception(e, user_msg="User action required")
        
        # Check if the function was called correctly with user message
        mock_log.assert_called_with("User action required: <ValueError> Invalid value", "error")
