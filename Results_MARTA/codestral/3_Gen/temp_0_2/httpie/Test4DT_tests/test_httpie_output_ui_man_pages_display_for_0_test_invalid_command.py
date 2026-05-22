
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

    Example:
        To display the man page for the 'http' command, you would call:
        
        >>> display_for(env=my_environment, program='http')
        
        If 'program' is a URL or a local command that has a man page, it will open the corresponding man page in your system's default viewer.
    """
    subprocess.run(
        [MAN_COMMAND, MAN_PAGE_SECTION, program],
        stdout=env.stdout,
        stderr=env.stderr
    )

@pytest.fixture
def mock_environment():
    env = MagicMock()
    return env

@patch('httpie.output.ui.man_pages.MAN_COMMAND', 'man')
@patch('httpie.output.ui.man_pages.MAN_PAGE_SECTION', '1')
def test_invalid_command(mock_environment):
    with pytest.raises(FileNotFoundError):
        display_for(env=mock_environment, program='invalid_command')
