
import pytest
from pathlib import Path
import sys
from unittest.mock import patch, MagicMock

# Import the function from the module
from httpie.context import Environment

@pytest.fixture(autouse=True)
def mock_sys_stdin():
    with patch('sys.stdin', new_callable=MagicMock):
        yield

@pytest.fixture(autouse=True)
def mock_sys_stdout():
    with patch('sys.stdout', new_callable=MagicMock):
        yield

@pytest.fixture(autouse=True)
def mock_sys_stderr():
    with patch('sys.stderr', new_callable=MagicMock):
        yield

# Test cases for Environment class
class TestEnvironment:
    
    def test_environment_default_attributes(self):
        env = Environment()
        assert env.is_windows is not None
        assert isinstance(env.config_dir, Path)