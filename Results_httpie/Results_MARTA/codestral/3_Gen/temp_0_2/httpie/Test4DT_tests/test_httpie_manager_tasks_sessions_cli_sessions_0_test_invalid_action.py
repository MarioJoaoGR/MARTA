
import pytest
from httpie.sessions import Environment
from httpie.manager.tasks.sessions import cli_sessions, ExitStatus
import argparse
from unittest.mock import patch

def test_invalid_action():
    env = Environment()
    args = argparse.Namespace(cli_sessions_action='unknown_action')
    
    with pytest.raises(ValueError):
        cli_sessions(env, args)
