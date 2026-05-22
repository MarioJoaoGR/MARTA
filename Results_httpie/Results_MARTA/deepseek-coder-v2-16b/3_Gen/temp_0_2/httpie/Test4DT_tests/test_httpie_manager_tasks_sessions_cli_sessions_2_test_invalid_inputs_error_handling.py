
import pytest
from unittest.mock import patch
from httpie.manager.tasks.sessions import cli_sessions, Environment, ExitStatus
import argparse

def test_invalid_inputs_error_handling():
    env = Environment()
    args = argparse.Namespace(cli_sessions_action='unexpected_action')
    
    with pytest.raises(ValueError) as excinfo:
        cli_sessions(env, args)
        
    assert str(excinfo.value) == 'Unexpected action: unexpected_action'
