
import pytest
from unittest.mock import patch
from io import StringIO
from httpie.output.writer import write_stream_with_colors_win

@pytest.fixture(autouse=True)
def mock_colorama():
    with patch('httpie.output.writer.colorama') as mock_colorama:
        yield

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
============================ no tests ran in 0.25s =============================
"""