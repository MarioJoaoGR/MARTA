
import pytest
from unittest.mock import patch
from httpie.manager.compat import PipError

def test_valid_inputs():
    # Test with valid inputs
    stdout = "Valid Standard Output"
    stderr = "Valid Standard Error"
    
    try:
        raise PipError(stdout, stderr)
    except PipError as e:
        assert e.stdout == stdout
        assert e.stderr == stderr
