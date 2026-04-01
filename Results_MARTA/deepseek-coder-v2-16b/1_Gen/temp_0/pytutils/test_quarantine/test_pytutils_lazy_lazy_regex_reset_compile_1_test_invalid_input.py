
import pytest
from unittest.mock import patch
from pytutils.lazy.lazy_regex import reset_compile as original_reset_compile

@pytest.fixture(autouse=True)
def reset_original_re_compile():
    with patch('pytutils.lazy.lazy_regex.re.compile', autospec=True) as mock_re_compile:
        yield
        # Restore the original re.compile function at the end of each test
        mock_re_compile.reset_mock()

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
============================ no tests ran in 0.04s =============================
"""