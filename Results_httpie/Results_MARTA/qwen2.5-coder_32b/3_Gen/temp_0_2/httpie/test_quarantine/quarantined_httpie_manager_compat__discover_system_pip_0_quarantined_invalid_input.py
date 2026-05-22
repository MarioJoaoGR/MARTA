
import subprocess
from typing import List, Optional
from unittest.mock import patch
from contextlib import suppress
import shutil

def _discover_system_pip() -> List[str]:
    """
    Discover the location of the system-wide pip executable.

    This function searches for the 'pip' or 'pip3' executable in the system PATH and checks its version to determine if it is compatible with Python 3. If a compatible pip executable is found, it returns its path; otherwise, it raises a SystemError indicating that no suitable pip executable was found.

    Parameters:
        None

    Returns:
        List[str]: A list containing the path to the system-wide pip executable.

    Raises:
        SystemError: If no compatible 'pip' or 'pip3' executable is found in the system PATH.

    Examples:
        To use this function, simply call it within your Python script:
        
        ```python
        try:
            pip_location = _discover_system_pip()
            print(f"Found pip at: {pip_location}")
        except SystemError as e:
            print(e)
        ```

    This function is crucial for ensuring that the correct version of 'pip' is used when installing CLI plugins. It helps to avoid issues related to incompatible or missing pip installations, which could otherwise lead to errors during plugin installation. By locating and verifying the presence of a compatible pip executable, this function supports a reliable mechanism for managing external dependencies in environments where such management is necessary.
    """
    
    def _check_pip_version(pip_location: Optional[str]) -> bool:
        if not pip_location:
            return False

        with suppress(subprocess.CalledProcessError):
            stdout = subprocess.check_output([pip_location, "--version"], text=True)
            return "python 3" in stdout

    targets = [
        "pip",
        "pip3"
    ]
    for target in targets:
        pip_location = shutil.which(target)
        if _check_pip_version(pip_location):
            return pip_location

    raise SystemError("Couldn't find 'pip' executable. Please ensure that pip in your system is available.")

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
report saved to: pytest_report_qwen2.5-coder_32b.json
============================ no tests ran in 0.13s =============================
"""