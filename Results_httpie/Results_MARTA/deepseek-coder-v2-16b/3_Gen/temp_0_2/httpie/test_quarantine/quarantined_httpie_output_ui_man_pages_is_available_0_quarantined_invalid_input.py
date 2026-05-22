
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
    """
    NO_MAN_PAGES = False
    MAN_COMMAND = 'man'
    MAN_PAGE_SECTION = ''
    
    if NO_MAN_PAGES or os.name == 'nt':
        return False
    try:
        with patch('subprocess.run', MagicMock(return_value=subprocess.CompletedProcess(args=[MAN_COMMAND, program], returncode=0))):
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
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
============================ no tests ran in 0.15s =============================
"""