
import pytest
from sanic.exceptions import Unauthorized


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_Unauthorized___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        with pytest.raises(Unauthorized) as excinfo:
            raise Unauthorized("Auth required.", scheme=None)
    
        assert str(excinfo.value) == "Auth required."
>       assert "WWW-Authenticate" not in excinfo.value.headers
E       AttributeError: 'Unauthorized' object has no attribute 'headers'

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_Unauthorized___init___0.py:10: AttributeError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(Unauthorized) as excinfo:
            raise Unauthorized("Auth required.", scheme="Unsupported")
    
        assert str(excinfo.value) == "Auth required."
>       assert "WWW-Authenticate" not in excinfo.value.headers
E       AssertionError: assert 'WWW-Authenticate' not in {'WWW-Authenticate': 'Unsupported'}
E        +  where {'WWW-Authenticate': 'Unsupported'} = Unauthorized('Auth required.').headers
E        +    where Unauthorized('Auth required.') = <ExceptionInfo Unauthorized('Auth required.') tblen=1>.value

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_Unauthorized___init___0.py:17: AssertionError
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_Unauthorized___init___0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_Unauthorized___init___0.py::test_invalid_inputs
======================== 2 failed, 5 warnings in 0.13s =========================
"""