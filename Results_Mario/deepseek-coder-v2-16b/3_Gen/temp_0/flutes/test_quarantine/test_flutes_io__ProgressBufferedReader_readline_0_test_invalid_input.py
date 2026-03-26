
import io
from unittest import mock
import pytest
from flutes.io import _ProgressBufferedReader

@pytest.fixture
def setup_reader():
    raw = io.BytesIO(b'some data')  # Use BytesIO for in-memory testing without fileno()
    bar_fn = mock.MagicMock()
    return _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.08s =============================

"""