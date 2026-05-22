
import subprocess
from unittest.mock import patch, MagicMock

def display_for(env: Environment, program: str) -> None:
    """
    Open the system man page for the given command (http/https/httpie).

    Parameters:
        env (Environment): An environment object that provides stdout and stderr streams.
        program (str): The name of the command whose man page you want to display. This can be a URL or a local command.

    Returns:
        None
    """
    with patch('subprocess.run') as mock_run:
        # Create a MagicMock for the Environment object
        env_mock = MagicMock()
        env_mock.stdout = subprocess.PIPE
        env_mock.stderr = subprocess.PIPE

        # Call the function with the mocked environment
        display_for(env=env_mock, program='http')

        # Assert that subprocess.run was called with the correct arguments
        mock_run.assert_called_once_with(
            [MAN_COMMAND, MAN_PAGE_SECTION, 'http'],
            stdout=env_mock.stdout,
            stderr=env_mock.stderr
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_ui_man_pages_display_for_1_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_man_pages_display_for_1_test_valid_input.py:5:21: E0602: Undefined variable 'Environment' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_man_pages_display_for_1_test_valid_input.py:27:13: E0602: Undefined variable 'MAN_COMMAND' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_man_pages_display_for_1_test_valid_input.py:27:26: E0602: Undefined variable 'MAN_PAGE_SECTION' (undefined-variable)


"""