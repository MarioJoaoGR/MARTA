
import sys
from pathlib import Path
from typing import Iterable, Iterator
import os

def _load_directories(site_dirs: Iterable[Path]) -> Iterator[None]:
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
report saved to: pytest_report_codestral.json
============================ no tests ran in 0.13s =============================
"""