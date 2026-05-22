
import sys
from pathlib import Path
from typing import Iterable, Iterator
import os

def _load_directories(site_dirs: Iterable[Path]) -> Iterator[None]:
    """
    Dynamically adds directories from a list of Path objects to the Python path and yields control,
    then removes those directories from the Python path after yielding.

    Parameters:
        site_dirs (Iterable[Path]): An iterable containing Path objects representing directories to be added to the Python path.

    Returns:
        Iterator[None]: An iterator that does not yield any values; its purpose is to execute side effects, specifically modifying the Python path and removing the added directories after yielding control.

    Example:
        To use this function, you would call it with a list of Path objects representing the directories you want to include in the Python path temporarily. For example:
        
        ```python
        from pathlib import Path
        site_dirs = [Path('/path/to/site1'), Path('/path/to/site2')]
        for _ in _load_directories(site_dirs):
            # The function modifies the Python path and then removes it after yielding.
            pass
        ```
    """
    plugin_dirs = [os.fspath(site_dir) for site_dir in site_dirs]
    sys.path.extend(plugin_dirs)
    try:
        yield
    finally:
        for plugin_dir in plugin_dirs:
            sys.path.remove(plugin_dir)

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
============================ no tests ran in 0.14s =============================
"""