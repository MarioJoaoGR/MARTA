
import pytest
from sanic import Sanic
from sanic.cookies import _quote

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_cookies__quote_0.py F [100%]

=================================== FAILURES ===================================
______________________________ test__quote_basic _______________________________

    def test__quote_basic():
        # Test when input string does not need quoting
        assert _quote("hello") == 'hello'
    
        # Test when input string needs quoting
        assert _quote('hello world') == '"hello world"'
    
        # Test with a string containing special characters that need escaping
>       assert _quote('hello;world') == '"hello\;world"'
E       assert '"hello\\073world"' == '"hello\\;world"'
E         
E         - "hello\;world"
E         ?        ^
E         + "hello\073world"
E         ?        ^^^

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_cookies__quote_0.py:14: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_cookies__quote_0.py:14
  /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_cookies__quote_0.py:14: DeprecationWarning: invalid escape sequence '\;'
    assert _quote('hello;world') == '"hello\;world"'

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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_cookies__quote_0.py::test__quote_basic
======================== 1 failed, 6 warnings in 0.13s =========================
"""