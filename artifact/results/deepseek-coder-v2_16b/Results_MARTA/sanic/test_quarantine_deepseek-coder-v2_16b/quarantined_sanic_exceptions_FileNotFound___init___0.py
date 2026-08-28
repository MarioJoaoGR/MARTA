
import pytest
from sanic.exceptions import FileNotFound


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_FileNotFound___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Arrange
        path = "/local/file/path"
        message = "The requested file was not found."
    
        # Act & Assert
        with pytest.raises(FileNotFound) as excinfo:
            raise FileNotFound(message, path, relative_url=None)
>       assert str(excinfo.value) == f"{message} Path: {path}"
E       AssertionError: assert 'The requeste...as not found.' == 'The requeste...cal/file/path'
E         
E         - The requested file was not found. Path: /local/file/path
E         + The requested file was not found.

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_FileNotFound___init___0.py:13: AssertionError
_________________________ test_missing_lines_to_cover __________________________

    def test_missing_lines_to_cover():
        # Arrange
        path = "/local/file/path"
        message = "The requested file was not found."
    
        # Act & Assert
        with pytest.raises(FileNotFound) as excinfo:
            raise FileNotFound(message, path, relative_url=None)
>       assert str(excinfo.value) == f"{message} Path: {path}"
E       AssertionError: assert 'The requeste...as not found.' == 'The requeste...cal/file/path'
E         
E         - The requested file was not found. Path: /local/file/path
E         + The requested file was not found.

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_FileNotFound___init___0.py:23: AssertionError
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_FileNotFound___init___0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_exceptions_FileNotFound___init___0.py::test_missing_lines_to_cover
======================== 2 failed, 5 warnings in 0.16s =========================
"""