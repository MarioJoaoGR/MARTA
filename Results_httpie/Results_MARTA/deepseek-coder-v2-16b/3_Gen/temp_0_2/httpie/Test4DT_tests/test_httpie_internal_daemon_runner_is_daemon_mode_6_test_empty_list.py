
import pytest
from unittest.mock import patch
from httpie.internal.daemon_runner import is_daemon_mode

def test_empty_list():
    with patch('httpie.internal.daemon_runner.is_daemon_mode') as mock_is_daemon_mode:
        mock_is_daemon_mode.return_value = False
        assert not is_daemon_mode([])
