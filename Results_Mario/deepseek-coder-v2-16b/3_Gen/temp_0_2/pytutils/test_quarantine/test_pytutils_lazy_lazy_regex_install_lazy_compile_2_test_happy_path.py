
import pytest
from unittest.mock import patch
from pytutils.lazy.lazy_regex import lazy_compile, reset_compile

@pytest.fixture(autouse=True)
def setup():
    with patch('re.compile', new=lazy_compile):
        yield  # This will run the test after the fixture is applied

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.06s =============================
"""