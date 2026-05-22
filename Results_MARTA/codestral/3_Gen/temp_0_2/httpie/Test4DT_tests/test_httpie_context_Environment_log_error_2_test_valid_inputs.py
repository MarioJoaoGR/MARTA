
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

def test_valid_inputs():
    with patch('httpie.context.Environment.stdin', new_callable=MagicMock) as mock_stdin:
        env = Environment()
        assert isinstance(env.stdin, MagicMock)
