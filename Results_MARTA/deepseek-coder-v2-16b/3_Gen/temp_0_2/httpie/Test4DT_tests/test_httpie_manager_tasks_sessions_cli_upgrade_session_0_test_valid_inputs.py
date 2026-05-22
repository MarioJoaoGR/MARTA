
import pytest
from unittest.mock import patch, MagicMock
from httpie.sessions import Environment
from httpie.manager.tasks.sessions import cli_upgrade_session, ExitStatus
import argparse

@pytest.fixture
def setup():
    env = Environment()
    args = argparse.Namespace(hostname='example.com', session='session123')
    return env, args

def test_valid_inputs(setup):
    env, args = setup
    
    with patch('httpie.manager.tasks.sessions.upgrade_session') as mock_upgrade:
        # Mock the upgrade_session function to return a successful status
        mock_upgrade.return_value = ExitStatus.SUCCESS
        
        result = cli_upgrade_session(env, args)
        
        assert result == ExitStatus.SUCCESS
