
import pytest
from unittest.mock import patch, MagicMock
import subprocess

def display_for(env: Environment, program: str) -> None:
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

@pytest.fixture
def mock_environment():
    env = MagicMock()
    return env

@pytest.mark.parametrize("program", ["invalid_command", "http://invalid-url"])
def test_invalid_command(mock_environment, program):
    with patch('subprocess.run', side_effect=FileNotFoundError("Command not found")):
        with pytest.raises(FileNotFoundError):
            display_for(env=mock_environment, program=program)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_ui_man_pages_display_for_1_test_invalid_command
httpie/Test4DT_tests_codestral/test_httpie_output_ui_man_pages_display_for_1_test_invalid_command.py:6:21: E0602: Undefined variable 'Environment' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_output_ui_man_pages_display_for_1_test_invalid_command.py:18:9: E0602: Undefined variable 'MAN_COMMAND' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_output_ui_man_pages_display_for_1_test_invalid_command.py:18:22: E0602: Undefined variable 'MAN_PAGE_SECTION' (undefined-variable)


"""