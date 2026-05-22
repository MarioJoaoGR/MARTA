
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.check_updates import cli_check_updates, Environment, ExitStatus

@pytest.fixture
def mock_env():
    env = MagicMock()
    env.config = {'version_info_file': 'fake_file'}
    return env

@pytest.fixture
def mock_args():
    args = MagicMock()
    args.lazy = False
    return args

def test_cli_check_updates(mock_env, mock_args):
    with patch('httpie.manager.tasks.check_updates.fetch_updates') as fetch_patch:
        with patch('httpie.manager.tasks.check_updates.get_update_status') as get_patch:
            fetch_patch.return_value = None
            get_patch.return_value = 'up-to-date'
            
            result = cli_check_updates(mock_env, mock_args)
            
            assert result == ExitStatus.SUCCESS
            fetch_patch.assert_called_once_with(mock_env, lazy=False)
            get_patch.assert_called_once_with(mock_env)
