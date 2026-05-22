
import subprocess
from unittest.mock import patch, MagicMock
import pytest
from httpie.output.ui.man_pages import MAN_COMMAND, MAN_PAGE_SECTION

def display_for(env: 'Environment', program: str) -> None:
    """
    Open the system man page for the given command (http/https/httpie).

    Parameters:
        env (Environment): An environment object that provides stdout and stderr streams.
        program (str): The name of the command whose man page you want to display. This can be a URL or a local command.

    Returns:
        None
    """
    subprocess.run(
        [MAN_COMMAND, MAN_PAGE_SECTION, program],
        stdout=env.stdout,
        stderr=env.stderr
    )

@pytest.mark.parametrize("program", ["http", "https", "httpie"])
def test_invalid_command(program):
    with patch('subprocess.run') as mock_run:
        env = MagicMock()
        display_for(env, program)
        
        # Assert that subprocess.run was called with the correct arguments
        mock_run.assert_called_once_with(
            [MAN_COMMAND, MAN_PAGE_SECTION, program],
            stdout=env.stdout,
            stderr=env.stderr
        )
