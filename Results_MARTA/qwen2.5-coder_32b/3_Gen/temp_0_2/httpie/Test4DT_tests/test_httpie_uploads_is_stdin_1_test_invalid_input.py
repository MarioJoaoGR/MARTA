
import sys
from unittest.mock import patch
from io import StringIO

def test_invalid_input():
    with patch('sys.stdin', StringIO()):
        from httpie.uploads import is_stdin
        fake_stdin = StringIO("Example content")
        assert not is_stdin(fake_stdin)
