
import argparse
from httpie.manager.tasks.sessions import cli_upgrade_session, Environment, ExitStatus
from unittest.mock import patch

def test_cli_upgrade_session():
    env = Environment()
    args = argparse.Namespace(hostname='example.com', session='session1')
    
    with patch('httpie.manager.tasks.sessions.upgrade_session') as mock_upgrade_session:
        mock_upgrade_session.return_value = ExitStatus.SUCCESS
        
        result = cli_upgrade_session(env, args)
        
        assert result == ExitStatus.SUCCESS
