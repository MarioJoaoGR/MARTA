
import pytest
from typing import Optional, Tuple

# Assuming _host_re is a pre-defined regular expression for matching host and port
_host_re = re.compile(r'^([^:]+)(?::(\d+))?$')

def parse_host(host: str) -> Tuple[Optional[str], Optional[int]]:
    """Split host:port into hostname and port.
    :return: None in place of missing elements
    """
    m = _host_re.fullmatch(host)
    if not m:
        return None, None
    host, port = m.groups()
    return host.lower(), int(port) if port is not None else None

# Test cases for parse_host function
def test_parse_host_no_port():
    assert parse_host("example.com") == ('example.com', None)

def test_parse_host_empty_string():
    assert parse_host(":8080") == (None, 8080)

def test_parse_host_invalid_format():
    assert parse_host("example.com:") == ('example.com', None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____________ ERROR collecting test_sanic_headers_parse_host_1.py ______________
/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_parse_host_1.py:6: in <module>
    _host_re = re.compile(r'^([^:]+)(?::(\d+))?$')
E   NameError: name 're' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_parse_host_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""