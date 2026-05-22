
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.sessions import cli_upgrade_session, ExitStatus
from httpie.sessions import Environment
import argparse

@pytest.fixture
def mock_env():
    env = Environment()
    env.config_dir = "test_config_dir"
    return env

@pytest.fixture
def mock_args():
    args = argparse.Namespace(hostname="example.com", session="session1")
    return args

@patch('httpie.manager.tasks.sessions.upgrade_session')
def test_cli_upgrade_session_valid_inputs(mock_upgrade_session, mock_env, mock_args):
    # Mock the upgrade_session function to return a successful status
    mock_upgrade_session.return_value = ExitStatus.SUCCESS
    
    result = cli_upgrade_session(mock_env, mock_args)
    
    assert result == ExitStatus.SUCCESS
