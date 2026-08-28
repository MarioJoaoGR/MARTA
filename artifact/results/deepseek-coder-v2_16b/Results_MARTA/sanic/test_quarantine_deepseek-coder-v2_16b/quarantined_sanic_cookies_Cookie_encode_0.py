
import pytest
from sanic.cookies import Cookie

def _is_legal_key(key):
    # This is a placeholder for the actual implementation of _is_legal_key function
    # For testing purposes, let's assume it checks if the key contains only legal characters (alphanumeric and underscore)
    return all(c.isalnum() or c == '_' for c in key)

class TestCookie:
    
    def test_illegal_characters_in_key(self):
        with pytest.raises(KeyError):
            Cookie('user-name', 'admin')
            
    def test_reserved_word_as_key(self):
        with pytest.raises(KeyError):
            Cookie('expires', 'admin')
    
    def test_valid_cookie(self):
        cookie = Cookie('username', 'admin')
        assert cookie.key == 'username'
        assert cookie.value == 'admin'
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_cookies_Cookie_encode_0.py F [ 33%]
..                                                                       [100%]

=================================== FAILURES ===================================
__________________ TestCookie.test_illegal_characters_in_key ___________________

self = <test_sanic_cookies_Cookie_encode_0.TestCookie object at 0x7f0ec61cded0>

    def test_illegal_characters_in_key(self):
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_cookies_Cookie_encode_0.py:13: Failed
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_cookies_Cookie_encode_0.py::TestCookie::test_illegal_characters_in_key
=================== 1 failed, 2 passed, 5 warnings in 0.14s ====================
"""