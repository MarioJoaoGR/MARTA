
import os
import sys
from unittest.mock import patch, Mock
from httpie.internal.daemons import _spawn_posix

def test_invalid_inputs():
    with patch('httpie.internal.daemons._spawn_posix', new=Mock()):
        # Test invalid inputs by passing None to args and process_context
        try:
            _spawn_posix(None, None)
        except TypeError as e:
            assert str(e) == "_spawn_posix() missing 2 required positional arguments: 'args' and 'process_context'"
