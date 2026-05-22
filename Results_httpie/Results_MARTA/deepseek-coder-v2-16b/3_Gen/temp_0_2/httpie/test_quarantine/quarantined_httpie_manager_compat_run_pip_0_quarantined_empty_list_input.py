
import sys
from unittest import mock
from httpie.manager.compat import List, is_frozen, _discover_system_pip, _run_pip_subprocess

def run_pip(args: List[str]) -> bytes:
    """Executes a pip subprocess with the given arguments.

    This function determines the appropriate pip executable to use based on whether the script is frozen or not, and then runs the specified pip command with the provided arguments. It supports both system-wide pip installations and virtual environments managed by `virtualenv` or similar tools. The function is designed to facilitate the installation of Python packages via a subprocess call, making it useful for automating package management tasks in various environments.

    Parameters:
        args (List[str]): A list of strings representing the arguments for the pip command. These include the action to perform (e.g., 'install', 'uninstall') followed by package names or other options as needed. For example, `['install', 'package_name']`.

    Returns:
        bytes: The standard output captured from the subprocess as a byte string.

    Raises:
        PipError: If the pip command exits with an error status code, this exception is raised with the stdout and stderr messages from the failed command.

    Examples:
        To install a package using run_pip:
        
        ```python
        try:
            output = run_pip(['install', 'numpy'])
            print(output)
        except PipError as e:
            print(f"Pip command failed with output:\n{e.stdout}\n{e.stderr}")
        ```
        
        In this example, the function `run_pip` is used to install the 'numpy' package using the system-wide pip executable if available, or else it uses the Python executable in the current environment to run the pip command. If the installation fails, an error message indicating the failure is printed.
    """
    if is_frozen:
        pip_executable = [_discover_system_pip()]
    else:
        pip_executable = [sys.executable, '-m', 'pip']

    return _run_pip_subprocess(pip_executable, args)

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
============================ no tests ran in 0.08s =============================
"""