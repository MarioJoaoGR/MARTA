
import pytest
from unittest.mock import patch
from httpie.status import ExitStatus, http_status_to_exit_status

def test_valid_input_happy_path():
    with patch('httpie.status.ExitStatus', new=ExitStatus):
        # Test valid 2xx status code without follow redirect
        assert http_status_to_exit_status(200) == ExitStatus.SUCCESS
        
        # Test valid 3xx status code with follow redirect
        assert http_status_to_exit_status(301, follow=True) == ExitStatus.SUCCESS
        
        # Test valid 4xx status code without follow redirect
        assert http_status_to_exit_status(404) == ExitStatus.ERROR_HTTP_4XX
        
        # Test valid 5xx status code without follow redirect
        assert http_status_to_exit_status(503) == ExitStatus.ERROR_HTTP_5XX
