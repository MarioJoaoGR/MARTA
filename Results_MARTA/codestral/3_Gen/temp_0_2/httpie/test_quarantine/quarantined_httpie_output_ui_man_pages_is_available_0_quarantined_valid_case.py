
import subprocess
import os
from unittest.mock import patch

def is_available(program: str) -> bool:
    """
    Check whether `program`'s man pages are available on this system.

    This function determines if the manual page for a given program exists by attempting to execute a command that would display the man page, such as 'man <program>'. It returns True if the man page is available and False otherwise. The function handles cases where there might be no man pages installed or if the system is Windows (where the concept of man pages does not exist).

    Parameters:
        program (str): The name of the program for which to check the availability of its man pages. This should typically be a command-line tool or utility.

    Returns:
        bool: True if the man pages for `program` are available on this system, False otherwise.

    Examples:
        >>> is_available("ls")  # Assuming 'man ls' would return 0 (success) on Unix systems with a man page installed
        True
        >>> is_available("python3")  # Python itself does not have man pages, so this would return False
        False
    """
    if NO_MAN_PAGES or os.name == 'nt':
        return False
    try:
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = subprocess.CompletedProcess(args=[MAN_COMMAND, MAN_PAGE_SECTION, program], returncode=0)
            result = is_available(program)
            assert result is True
    except Exception:
        # There might be some errors outside the process, e.g
        # a permission error to execute something that is not an
        # executable.
        return False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_ui_man_pages_is_available_0_test_valid_case
httpie/Test4DT_tests_codestral/test_httpie_output_ui_man_pages_is_available_0_test_valid_case.py:24:7: E0602: Undefined variable 'NO_MAN_PAGES' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_output_ui_man_pages_is_available_0_test_valid_case.py:28:70: E0602: Undefined variable 'MAN_COMMAND' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_output_ui_man_pages_is_available_0_test_valid_case.py:28:83: E0602: Undefined variable 'MAN_PAGE_SECTION' (undefined-variable)


"""