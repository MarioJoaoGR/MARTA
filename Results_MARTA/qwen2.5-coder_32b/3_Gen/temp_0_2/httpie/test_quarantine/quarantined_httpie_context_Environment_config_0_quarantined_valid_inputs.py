
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

@pytest.fixture(autouse=True)
def mock_environment():
    with patch('httpie.context.sys') as sys_mock:
        stdin_mock = MagicMock()
        stdout_mock = MagicMock()
        stderr_mock = MagicMock()
        
        sys_mock.stdin = stdin_mock
        sys_mock.stdout = stdout_mock
        sys_mock.stderr = stderr_mock
        
        env = Environment(devnull=None)
        yield env

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
============================ no tests ran in 0.12s =============================
"""