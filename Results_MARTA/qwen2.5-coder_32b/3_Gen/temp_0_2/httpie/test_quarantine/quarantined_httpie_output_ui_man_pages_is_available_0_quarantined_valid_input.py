
import subprocess
import os
from unittest.mock import patch, MagicMock

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
        process = subprocess.run(
            [MAN_COMMAND, MAN_PAGE_SECTION, program],
            shell=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception:
        # There might be some errors outside the process, e.g
        # a permission error to execute something that is not an
        # executable.
        return False
    else:
        return process.returncode == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_ui_man_pages_is_available_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_man_pages_is_available_0_test_valid_input.py:24:7: E0602: Undefined variable 'NO_MAN_PAGES' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_man_pages_is_available_0_test_valid_input.py:28:13: E0602: Undefined variable 'MAN_COMMAND' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_man_pages_is_available_0_test_valid_input.py:28:26: E0602: Undefined variable 'MAN_PAGE_SECTION' (undefined-variable)


"""