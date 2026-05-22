
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

@pytest.fixture(autouse=True)
def mock_environment():
    with patch('httpie.context.sys') as sys_mock, \
         patch('httpie.context.curses') as curses_mock, \
         patch('httpie.context.colorama.initialise') as colorama_mock:
        # Mocking the behavior of sys module
        sys_mock.stdin = MagicMock()
        sys_mock.stdout = MagicMock()
        sys_mock.stderr = MagicMock()
        sys_mock.stdin.isatty.return_value = True  # Example return value
        sys_mock.stdout.isatty.return_value = True  # Example return value
        sys_mock.stderr.isatty.return_value = True  # Example return value
        
        # Mocking the behavior of curses module
        curses_mock.tigetnum.return_value = 256  # Example return value
        
        # Mocking the behavior of colorama module
        colorama_mock.wrap_stream.side_effect = lambda stream, **kwargs: stream
        
        yield Environment()

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
============================ no tests ran in 0.19s =============================
"""