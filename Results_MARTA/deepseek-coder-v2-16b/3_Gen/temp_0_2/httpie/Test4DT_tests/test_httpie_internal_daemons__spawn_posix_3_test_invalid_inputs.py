
import os
import sys
import platform
from contextlib import suppress
from unittest.mock import patch
from httpie.internal.daemons import _spawn_posix

def test_invalid_inputs():
    with patch('httpie.internal.daemons._start_process', autospec=True) as mock_start_process:
        # Test invalid inputs by passing None to args and process_context
        with patch.dict(os.environ, {}, clear=True):
            try:
                _spawn_posix(None, None)
            except SystemExit as e:
                assert e.code == 0
