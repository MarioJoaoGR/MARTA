
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.sessions import cli_upgrade_all_sessions, ExitStatus
from httpie.sessions import Environment
import argparse

@pytest.fixture
def mock_env():
    env = MagicMock(spec=Environment)
    env.config_dir = MagicMock()
    env.config_dir.iterdir = lambda: [MagicMock()]
    return env

@pytest.fixture
def mock_args():
    args = argparse.Namespace(cli_sessions_action='upgrade-all')
    return args

def test_valid_inputs(mock_env, mock_args):
    with patch('httpie.manager.tasks.sessions.SESSIONS_DIR_NAME', 'sessions'):
        with patch('httpie.manager.tasks.sessions.upgrade_session') as mock_upgrade:
            # Mock the return value of upgrade_session to always return ExitStatus.SUCCESS
            mock_upgrade.return_value = ExitStatus.SUCCESS
            
            result = cli_upgrade_all_sessions(mock_env, mock_args)
            
            assert result == ExitStatus.SUCCESS
