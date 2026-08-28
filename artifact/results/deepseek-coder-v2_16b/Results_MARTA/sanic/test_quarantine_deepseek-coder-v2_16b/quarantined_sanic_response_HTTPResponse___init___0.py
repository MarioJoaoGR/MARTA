
from sanic.response import HTTPResponse
import pytest


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_response_HTTPResponse___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        response = HTTPResponse(body=b'Hello, World!', status=200, headers={'Content-Type': 'text/plain'}, content_type='text/html')
    
        assert response.status == 200
>       assert response.headers['Content-Type'] == 'text/html'
E       AssertionError: assert 'text/plain' == 'text/html'
E         
E         - text/html
E         + text/plain

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_response_HTTPResponse___init___0.py:9: AssertionError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        response = HTTPResponse(body=None, status=0, headers={}, content_type=None)
    
>       assert response.status == 200
E       assert 0 == 200
E        +  where 0 = <sanic.response.HTTPResponse object at 0x7ffbbf459000>.status

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_response_HTTPResponse___init___0.py:14: AssertionError
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_response_HTTPResponse___init___0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_response_HTTPResponse___init___0.py::test_edge_cases
======================== 2 failed, 5 warnings in 0.30s =========================
"""