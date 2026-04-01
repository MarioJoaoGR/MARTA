
import pytest
from unittest.mock import patch, MagicMock
from flutes.exception import log_exception
import subprocess
import traceback

@pytest.mark.parametrize("e, user_msg, kwargs", [
    (ValueError("Invalid value"), None, {}),
    (RuntimeError("Operation failed"), "User action required", {})
])
def test_log_exception(e, user_msg, kwargs):
    with patch('flutes.exception.log') as mock_log:
        log_exception(e, user_msg=user_msg, **kwargs)
        
        # Check if the exception message is logged correctly
        expected_exc_msg = f"<{e.__class__.__qualname__}> {e}"
        if user_msg:
            expected_exc_msg = f"{user_msg}: {expected_exc_msg}"
        
        mock_log.assert_called_with(expected_exc_msg, "error", **kwargs)
