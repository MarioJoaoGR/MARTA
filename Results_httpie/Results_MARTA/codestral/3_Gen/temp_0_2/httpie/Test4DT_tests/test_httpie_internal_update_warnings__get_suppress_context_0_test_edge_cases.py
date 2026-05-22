
import pytest
from unittest.mock import patch, MagicMock
from contextlib import nullcontext
from httpie.internal.update_warnings import _get_suppress_context

def test_get_suppress_context_with_developer_mode_enabled():
    env = MagicMock()
    env.config.developer_mode = True
    
    with patch('httpie.internal.update_warnings._get_suppress_context', return_value=nullcontext()):
        ctx_mgr = _get_suppress_context(env)
        with pytest.raises(ValueError, match="Test Error"):
            with ctx_mgr:
                raise ValueError("Test Error")  # This should not be suppressed
