
import pytest
from sanic.headers import parse_host

@pytest.mark.parametrize("input_str, expected", [
    ("example.com", ('example.com', None)),
    ("example.com:8080", ('example.com', 8080)),
    ("192.168.1.1:3306", ('192.168.1.1', 3306)),
    (":8080", (None, 8080)),
    ("example.com:", ('example.com', None))
])
def test_parse_host_basic(input_str, expected):
    assert parse_host(input_str) == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_parse_host_0.py . [ 20%]
..FF                                                                     [100%]

=================================== FAILURES ===================================
____________________ test_parse_host_basic[:8080-expected3] ____________________

input_str = ':8080', expected = (None, 8080)

    @pytest.mark.parametrize("input_str, expected", [
        ("example.com", ('example.com', None)),
        ("example.com:8080", ('example.com', 8080)),
        ("192.168.1.1:3306", ('192.168.1.1', 3306)),
        (":8080", (None, 8080)),
        ("example.com:", ('example.com', None))
    ])
    def test_parse_host_basic(input_str, expected):
>       assert parse_host(input_str) == expected
E       assert (None, None) == (None, 8080)
E         
E         At index 1 diff: None != 8080
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_parse_host_0.py:13: AssertionError
________________ test_parse_host_basic[example.com:-expected4] _________________

input_str = 'example.com:', expected = ('example.com', None)

    @pytest.mark.parametrize("input_str, expected", [
        ("example.com", ('example.com', None)),
        ("example.com:8080", ('example.com', 8080)),
        ("192.168.1.1:3306", ('192.168.1.1', 3306)),
        (":8080", (None, 8080)),
        ("example.com:", ('example.com', None))
    ])
    def test_parse_host_basic(input_str, expected):
>       assert parse_host(input_str) == expected
E       AssertionError: assert (None, None) == ('example.com', None)
E         
E         At index 0 diff: None != 'example.com'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_parse_host_0.py:13: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13
../../../../../opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13
  /opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13: DeprecationWarning: websockets.WebSocketCommonProtocol is deprecated
    from websockets import (  # type: ignore

../../../../pydeps/marta/websockets/legacy/__init__.py:6
  /data/pydeps/marta/websockets/legacy/__init__.py:6: DeprecationWarning: websockets.legacy is deprecated; see https://websockets.readthedocs.io/en/stable/howto/upgrade.html for upgrade instructions
    warnings.warn(  # deprecated in 14.0 - 2024-11-09

../../../../../opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13
../../../../../opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13
  /opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13: DeprecationWarning: websockets.handshake is deprecated
    from websockets import (  # type: ignore

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_parse_host_0.py::test_parse_host_basic[:8080-expected3]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_parse_host_0.py::test_parse_host_basic[example.com:-expected4]
=================== 2 failed, 3 passed, 5 warnings in 0.16s ====================
"""