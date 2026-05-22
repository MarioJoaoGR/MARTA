
import pytest
from unittest.mock import patch
from httpie.manager.compat import PipError

def test_invalid_inputs():
    with pytest.raises(PipError):
        raise PipError("Invalid stdout", "Invalid stderr")
