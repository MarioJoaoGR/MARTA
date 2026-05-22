
import pytest
from unittest.mock import MagicMock, patch
from httpie.output.streams import PrettyStream

@pytest.fixture
def setup_pretty_stream():
    conversion = MagicMock()
    formatting = MagicMock()
    with patch('httpie.output.streams.PrettyStream.__init__', return_value=None):
        stream = PrettyStream(conversion, formatting)
        yield stream

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
============================ no tests ran in 0.13s =============================
"""