
import pytest
from sanic.exceptions import SanicException



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_SanicException___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        try:
>           raise SanicException("This is a test exception", status_code=404)
E           sanic.exceptions.SanicException: This is a test exception

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_SanicException___init___0.py:7: SanicException

During handling of the above exception, another exception occurred:

    def test_valid_inputs():
        try:
            raise SanicException("This is a test exception", status_code=404)
        except SanicException as e:
            assert str(e) == "This is a test exception"
            assert e.status_code == 404
>           assert e.quiet is None
E           AssertionError: assert True is None
E            +  where True = SanicException('This is a test exception').quiet

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_SanicException___init___0.py:11: AssertionError
______________________________ test_default_quiet ______________________________

    def test_default_quiet():
        try:
>           raise SanicException("Test default quiet", status_code=500)
E           sanic.exceptions.SanicException: Test default quiet

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_SanicException___init___0.py:15: SanicException

During handling of the above exception, another exception occurred:

    def test_default_quiet():
        try:
            raise SanicException("Test default quiet", status_code=500)
        except SanicException as e:
            assert str(e) == "Test default quiet"
            assert e.status_code == 500
>           assert e.quiet is True
E           AttributeError: 'SanicException' object has no attribute 'quiet'

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_SanicException___init___0.py:19: AttributeError
__________________________ test_explicitly_set_quiet ___________________________

    def test_explicitly_set_quiet():
        try:
>           raise SanicException("Explicitly set quiet to False", status_code=400, quiet=False)
E           sanic.exceptions.SanicException: Explicitly set quiet to False

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_SanicException___init___0.py:23: SanicException

During handling of the above exception, another exception occurred:

    def test_explicitly_set_quiet():
        try:
            raise SanicException("Explicitly set quiet to False", status_code=400, quiet=False)
        except SanicException as e:
            assert str(e) == "Explicitly set quiet to False"
            assert e.status_code == 400
>           assert e.quiet is False
E           AttributeError: 'SanicException' object has no attribute 'quiet'

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_SanicException___init___0.py:27: AttributeError
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_SanicException___init___0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_SanicException___init___0.py::test_default_quiet
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_SanicException___init___0.py::test_explicitly_set_quiet
======================== 3 failed, 5 warnings in 0.30s =========================
"""