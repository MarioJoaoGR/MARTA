
import pytest
from ansible.utils.py3compat import _TextEnviron
import os
import sys
from unittest.mock import patch

def test_valid_inputs():
    """Test that environment variables are correctly retrieved as text strings."""
    with patch.dict(os.environ, {"KEY": "VALUE"}):
        env = _TextEnviron()
        assert env["KEY"] == "VALUE"

