
import re
from typing import Tuple
from unittest.mock import patch

def parse_prefixed_json(data: str) -> Tuple[str, str]:
    """Find the potential JSON body from `data`.

    Sometimes the JSON body is prefixed with a XSSI magic string, specific to the server.
    Return a tuple (data prefix, actual JSON body).

    """
    match = re.match(r'^__XSSI_PREFIX__(.*)', data)
    if match:
        data_prefix = match.group(0)
        body = match.group(1)
        return data_prefix, body
    else:
        return '', data

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
============================ no tests ran in 0.11s =============================
"""