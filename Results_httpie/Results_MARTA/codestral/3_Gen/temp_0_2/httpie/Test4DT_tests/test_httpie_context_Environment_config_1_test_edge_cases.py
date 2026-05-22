
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

def test_edge_cases():
    with patch('httpie.context.Environment.config_dir', None):
        env = Environment()
        assert env.config_dir is None
