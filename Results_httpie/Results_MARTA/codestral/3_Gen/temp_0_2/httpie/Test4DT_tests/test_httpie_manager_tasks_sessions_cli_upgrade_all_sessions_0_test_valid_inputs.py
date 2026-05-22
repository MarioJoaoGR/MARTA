
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.sessions import cli_upgrade_all_sessions, ExitStatus
from httpie.sessions import Environment
import argparse

@pytest.fixture
def mock_env():
    env = Environment()
    env.config_dir = MagicMock()
    return env

@pytest.fixture
def mock_args():
    args = argparse.Namespace(loglevel='INFO')
    return args

def test_valid_inputs(mock_env, mock_args):
    # Mock the session directory and files
    mock_env.config_dir.iterdir.return_value = [MagicMock()]
    mock_env.config_dir.__truediv__.return_value = MagicMock()
    mock_env.config_dir.__truediv__().glob.return_value = [MagicMock()]
    
    # Mock the upgrade_session function to return SUCCESS for all sessions
    with patch('httpie.manager.tasks.sessions.upgrade_session', return_value=ExitStatus.SUCCESS):
        result = cli_upgrade_all_sessions(mock_env, mock_args)
        assert result == ExitStatus.SUCCESS
