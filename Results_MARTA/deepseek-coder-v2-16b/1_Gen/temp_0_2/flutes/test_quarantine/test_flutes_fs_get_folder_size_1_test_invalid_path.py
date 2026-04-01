
import subprocess
from pathlib import Path

def get_folder_size(path: Path) -> int:
    r"""Get disk usage (in bytes) of a specified folder.

This function takes a single argument, `path`, which is expected to be a path-like object representing the directory whose size you want to measure. The function uses the 'du' command-line utility to get the total size of the directory in bytes and returns this value as an integer.

Parameters:
    path (Path): A path-like object representing the directory for which to calculate the disk usage. This should be a string or any object that can be converted to a string representing a file system path.

Returns:
    int: The total size of the specified directory in bytes.

Example:
    To get the size of the folder '/home/user/documents', you would call the function like this:
    
    ```python
    from pathlib import Path
    print(get_folder_size(Path('/home/user/documents')))
    ```

This will output an integer representing the total disk usage in bytes of the '/home/user/documents' directory.
"""
    # Credit: https://stackoverflow.com/a/25574638/4909228
    r"""Get disk usage of given path in bytes."""
    return int(subprocess.check_output(['du', '-bs', str(path)]).split()[0].decode('utf-8'))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.05s =============================
"""