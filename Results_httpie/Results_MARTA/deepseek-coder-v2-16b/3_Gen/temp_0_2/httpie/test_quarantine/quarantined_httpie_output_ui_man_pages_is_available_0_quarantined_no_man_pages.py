
import subprocess
import os
from unittest.mock import patch, MagicMock

def is_available(program: str) -> bool:
    """
    Check whether `program`'s man pages are available on this system.

    This function determines if the manual page for a given program exists by attempting to execute a command that would display the man page such as 'man <program>'. It returns True if the man page is available and False otherwise. The function handles cases where there might be no man pages installed or if the system is Windows (where the concept of man pages does not exist).

    Parameters:
        program (str): The name of the program for which to check the availability of its man pages. This should typically be a command-line tool or utility.

    Returns:
        bool: True if the man pages for `program` are available on this system, False otherwise.
    """
    if NO_MAN_PAGES or os.name == 'nt':
        return False
    try:
        process = subprocess.run(
            [MAN_COMMAND, str(MAN_PAGE_SECTION), program],
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
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_ui_man_pages_is_available_0_test_no_man_pages
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_man_pages_is_available_0_test_no_man_pages.py:18:7: E0602: Undefined variable 'NO_MAN_PAGES' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_man_pages_is_available_0_test_no_man_pages.py:22:13: E0602: Undefined variable 'MAN_COMMAND' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_man_pages_is_available_0_test_no_man_pages.py:22:30: E0602: Undefined variable 'MAN_PAGE_SECTION' (undefined-variable)


"""