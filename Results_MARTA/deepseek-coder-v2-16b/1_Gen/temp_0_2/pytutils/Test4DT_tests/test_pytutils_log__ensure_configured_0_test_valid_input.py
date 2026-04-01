
import pytest
from unittest.mock import patch
from pytutils.log import configure

# Assuming _CONFIGURED is defined somewhere in pytutils.log or a related module
_CONFIGURED = [False]

def test_valid_input():
    with patch('pytutils.log.configure') as mock_configure:
        from pytutils.log import _ensure_configured, _CONFIGURED
        
        # First call should trigger configure() and set _CONFIGURED to True
        _ensure_configured()
        assert mock_configure.called
        assert _CONFIGURED[0] is True
        
        # Subsequent calls with the same _CONFIGURED should not call configure() again
        _ensure_configured()  # Should not trigger configure() again
        assert mock_configure.call_count == 1
