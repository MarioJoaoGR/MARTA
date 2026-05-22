
import subprocess
from unittest.mock import patch

def display_for(env: Environment, program: str) -> None:
    """
    Open the system man page for the given command (http/https/httpie).

    Parameters:
        env (Environment): An environment object that provides stdout and stderr streams.
        program (str): The name of the command whose man page you want to display. This can be a URL or a local command.

    Returns:
        None
    """
    with patch('subprocess.run'):
        subprocess.run([MAN_COMMAND, MAN_PAGE_SECTION, program], stdout=env.stdout, stderr=env.stderr)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_ui_man_pages_display_for_0_test_invalid_command
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_man_pages_display_for_0_test_invalid_command.py:5:21: E0602: Undefined variable 'Environment' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_man_pages_display_for_0_test_invalid_command.py:17:24: E0602: Undefined variable 'MAN_COMMAND' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_man_pages_display_for_0_test_invalid_command.py:17:37: E0602: Undefined variable 'MAN_PAGE_SECTION' (undefined-variable)


"""