
import pytest
from io import StringIO
from unittest.mock import patch
from httpie.output.writer import write_stream

@pytest.fixture(autouse=True)
def mock_stdout():
    with patch('httpie.output.writer.sys.stdout', new=StringIO()) as mock:
        yield mock

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
============================ no tests ran in 0.19s =============================
"""