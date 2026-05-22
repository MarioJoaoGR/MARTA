
import pytest
from unittest.mock import patch
from httpie.status import ExitStatus, http_status_to_exit_status

def test_valid_input_happy_path():
    with patch('httpie.status.ExitStatus', new=ExitStatus):
        # Test valid 2xx status codes when follow is False
        assert http_status_to_exit_status(200) == ExitStatus.SUCCESS
        assert http_status_to_exit_status(201) == ExitStatus.SUCCESS
        
        # Test valid 3xx status codes when follow is True
        assert http_status_to_exit_status(301, follow=True) == ExitStatus.SUCCESS
        
        # Test invalid or unrecognized status codes
        assert http_status_to_exit_status(404) == ExitStatus.ERROR_HTTP_4XX
        assert http_status_to_exit_status(503) == ExitStatus.ERROR_HTTP_5XX
        
        # Test valid 4xx status codes when follow is False
        assert http_status_to_exit_status(400) == ExitStatus.ERROR_HTTP_4XX
        assert http_status_to_exit_status(499) == ExitStatus.ERROR_HTTP_4XX
        
        # Test valid 5xx status codes when follow is False
        assert http_status_to_exit_status(500) == ExitStatus.ERROR_HTTP_5XX
        assert http_status_to_exit_status(599) == ExitStatus.ERROR_HTTP_5XX
