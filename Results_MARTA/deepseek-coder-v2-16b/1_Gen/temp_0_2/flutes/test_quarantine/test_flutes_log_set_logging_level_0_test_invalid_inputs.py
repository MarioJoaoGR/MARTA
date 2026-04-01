
import pytest
from unittest.mock import patch
from flutes.log import LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER
from typing import Any, Callable

# Assuming LoggingLevel is a type defined elsewhere in your codebase
LoggingLevel = str  # Example definition for demonstration purposes

@pytest.fixture(autouse=True)
def mock_logging():
    with patch('flutes.log._CONSOLE_LOGGING_LEVEL.value', new_callable=lambda: None):
        yield  # This is where the test will run

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