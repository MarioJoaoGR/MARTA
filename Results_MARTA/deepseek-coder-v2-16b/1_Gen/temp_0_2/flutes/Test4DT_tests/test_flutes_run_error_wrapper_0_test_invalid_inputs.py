
import pytest
import subprocess
from io import StringIO
from unittest.mock import patch
from flutes.run import error_wrapper

# Define ExcType as a placeholder for the actual exception type used in the function
ExcType = (subprocess.CalledProcessError, subprocess.TimeoutExpired)  # noqa: F821

@pytest.mark.parametrize("err", [
    pytest.param(subprocess.CalledProcessError(returncode=1, cmd='command', output=b'output'), id="CalledProcessError"),
    pytest.param(subprocess.TimeoutExpired(cmd='command', timeout=1), id="TimeoutExpired")
])
def test_invalid_inputs(err):
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        wrapped_error = error_wrapper(err)
        assert str(wrapped_error) == f"Command 'command' returned non-zero exit status 1.\nCaptured output:\n    output" if isinstance(err, subprocess.CalledProcessError) else "Command timed out after 1 seconds."
