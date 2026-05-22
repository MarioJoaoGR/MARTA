
import sys
from io import StringIO
import pytest
from unittest.mock import patch

def test_invalid_input():
    with patch('sys.stdin', StringIO("Example content")):
        from httpie.uploads import is_stdin
        fake_stdin = StringIO("Example content")
        assert not is_stdin(fake_stdin)
