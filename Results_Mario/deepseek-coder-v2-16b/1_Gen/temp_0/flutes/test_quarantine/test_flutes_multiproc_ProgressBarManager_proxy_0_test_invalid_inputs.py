
import pytest
from flutes.multiproc import ProgressBarManager
import multiprocessing as mp
import time
import random
from typing import List, Iterable, Dict, Optional, Any, Union, Literal, Iterator, overload

@pytest.fixture(scope="module")
def mock_flutes():
    manager = ProgressBarManager()
    yield manager
    # Clean up if necessary

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
============================ no tests ran in 0.08s =============================
"""