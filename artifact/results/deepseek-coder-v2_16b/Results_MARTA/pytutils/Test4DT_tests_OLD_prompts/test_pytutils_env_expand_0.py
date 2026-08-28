
import pytest
from unittest.mock import patch
import pytutils.env as env
import os

def test_expand_none():
    with patch('pytutils.env.os') as mock_os:
        mock_os.path.expandvars.return_value = None
        mock_os.path.expanduser.return_value = None
        assert env.expand(None) is None
