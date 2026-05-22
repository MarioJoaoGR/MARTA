
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.sessions import cli_sessions
from httpie.sessions import Environment
from argparse import Namespace
from enum import Enum

def test_invalid_inputs_error_handling():
    env = Environment()
    args = Namespace(cli_sessions_action='unexpected_action')
    
    with pytest.raises(ValueError) as excinfo:
        cli_sessions(env, args)
        
    assert str(excinfo.value) == "Unexpected action: unexpected_action"
