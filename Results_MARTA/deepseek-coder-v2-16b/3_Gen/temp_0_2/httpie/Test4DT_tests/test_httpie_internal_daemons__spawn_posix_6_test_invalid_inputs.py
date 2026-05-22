
import os
import sys
from httpie.internal.daemons import _spawn_posix
from unittest.mock import patch, MagicMock

def test_invalid_inputs():
    with patch('httpie.internal.daemons._start_process', new=MagicMock()):
        # Test invalid inputs by passing None to args and process_context
        try:
            _spawn_posix(None, None)
        except TypeError as e:
            assert str(e) == "_spawn_posix() missing 2 required positional arguments: 'args' and 'process_context'"
