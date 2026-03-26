
import io
import os
from flutes.io import _ProgressBufferedReader, BarFn
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def setup_reader(mock_bar_fn):
    raw = io.BytesIO(b'test data')
    reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=mock_bar_fn)
    return reader

@pytest.fixture
def mock_bar_fn():
    bar_fn = MagicMock()
    bar_fn.return_value.total = len(b'test data')
    return bar_fn

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