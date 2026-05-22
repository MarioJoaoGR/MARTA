
import pytest
from unittest.mock import patch
from httpie.manager.compat import PipError

def test_piperror_init():
    """Test that PipError initializes with stdout and stderr."""
    # Arrange
    stdout = "Standard Output Message"
    stderr = "Standard Error Message"
    
    # Act & Assert
    try:
        raise PipError(stdout, stderr)
    except PipError as e:
        assert e.stdout == stdout
        assert e.stderr == stderr
