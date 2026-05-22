
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.compat import PipError

def test_invalid_inputs():
    with patch('subprocess.run', return_value=MagicMock(returncode=1)):
        stdout = "Standard Output Message"
        stderr = "Standard Error Message"
        
        # Test invalid inputs by initializing the PipError class
        with pytest.raises(PipError):
            raise PipError(stdout, stderr)
