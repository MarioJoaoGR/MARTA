
import pytest
from unittest.mock import patch, MagicMock
from httpie.internal.daemon_runner import run_daemon_task, Environment, ExitStatus, DAEMONIZED_TASKS

@pytest.mark.parametrize("env, args", [
    (Environment(config={'developer_mode': False}), ['--daemon', '1234']),
    (Environment(config={'developer_mode': True}), ['--daemon', '1234'])
])
def test_invalid_inputs(env, args):
    with patch('httpie.internal.daemon_runner.redirect_stdout', lambda x: x), \
         patch('httpie.internal.daemon_runner.redirect_stderr', lambda x: x), \
         patch('httpie.internal.daemon_runner._get_suppress_context', return_value=MagicMock()):
        with pytest.raises(AssertionError):
            run_daemon_task(env, args)
