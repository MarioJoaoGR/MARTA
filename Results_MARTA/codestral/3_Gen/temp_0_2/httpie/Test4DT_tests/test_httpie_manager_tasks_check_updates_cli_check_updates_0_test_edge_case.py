
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.check_updates import cli_check_updates, Environment, ExitStatus

@pytest.fixture
def mock_env():
    # Create a mock Environment instance
    env = MagicMock(spec=Environment)
    return env

@pytest.fixture
def mock_args():
    # Create a mock argparse.Namespace instance
    args = MagicMock()
    args.lazy = True  # Default value for lazy argument
    return args

def test_cli_check_updates(mock_env, mock_args):
    with patch('httpie.manager.tasks.check_updates.fetch_updates') as fetch_patch:
        with patch('httpie.manager.tasks.check_updates.get_update_status') as get_patch:
            # Mock the return value of get_update_status
            mock_env.stdout = MagicMock()
            mock_env.stdout.write = MagicMock(return_value=None)
            get_patch.return_value = "Update status"  # Assuming get_update_status returns a string

            result = cli_check_updates(mock_env, mock_args)

            fetch_patch.assert_called_once_with(mock_env, lazy=False)
            mock_env.stdout.write.assert_called_once_with("Update status")
            assert result == ExitStatus.SUCCESS
