
import pytest
from typing import Dict, Union, Iterable
from urllib.parse import unquote
from sanic.headers import OptionsIterable

def fwd_normalize(fwd: OptionsIterable) -> Dict[str, Union[int, str]]:
    """Normalize and convert values extracted from forwarded headers."""
    ret: Dict[str, Union[int, str]] = {}
    for key, val in fwd:
        if val is not None:
            try:
                if key in ("by", "for"):
                    ret[key] = fwd_normalize_address(val)
                elif key in ("host", "proto"):
                    ret[key] = val.lower()
                elif key == "port":
                    ret[key] = int(val)
                elif key == "path":
                    ret[key] = unquote(val)
                else:
                    ret[key] = val
            except ValueError:
                pass
    return ret

def fwd_normalize_address(addr: str) -> str:
    """Normalize an address string."""
    return addr.lower()

# Test cases for valid inputs


# Test case for invalid input
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_input_1 ______________________________

    def test_valid_input_1():
        headers = {'by': 'Example Corp', 'host': 'example.com', 'port': '8080', 'path': 'foo%2Bar'}
>       result = fwd_normalize(OptionsIterable(headers))

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_1.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = typing.Iterable[typing.Tuple[str, str]]
args = ({'by': 'Example Corp', 'host': 'example.com', 'path': 'foo%2Bar', 'port': '8080'},)
kwargs = {}

    def __call__(self, *args, **kwargs):
        if not self._inst:
            raise TypeError(f"Type {self._name} cannot be instantiated; "
                            f"use {self.__origin__.__name__}() instead")
>       result = self.__origin__(*args, **kwargs)
E       TypeError: Iterable() takes no arguments

/opt/conda/envs/test4py_env/lib/python3.10/typing.py:957: TypeError
______________________________ test_valid_input_2 ______________________________

    def test_valid_input_2():
        headers = {'proto': 'HTTP/1.1', 'for': '[2001:db8::1]'}
>       result = fwd_normalize(OptionsIterable(headers))

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_1.py:39: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = typing.Iterable[typing.Tuple[str, str]]
args = ({'for': '[2001:db8::1]', 'proto': 'HTTP/1.1'},), kwargs = {}

    def __call__(self, *args, **kwargs):
        if not self._inst:
            raise TypeError(f"Type {self._name} cannot be instantiated; "
                            f"use {self.__origin__.__name__}() instead")
>       result = self.__origin__(*args, **kwargs)
E       TypeError: Iterable() takes no arguments

/opt/conda/envs/test4py_env/lib/python3.10/typing.py:957: TypeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        headers = {'port': 'not-a-number'}
        with pytest.raises(ValueError):
>           fwd_normalize(OptionsIterable(headers))

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_1.py:46: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = typing.Iterable[typing.Tuple[str, str]]
args = ({'port': 'not-a-number'},), kwargs = {}

    def __call__(self, *args, **kwargs):
        if not self._inst:
            raise TypeError(f"Type {self._name} cannot be instantiated; "
                            f"use {self.__origin__.__name__}() instead")
>       result = self.__origin__(*args, **kwargs)
E       TypeError: Iterable() takes no arguments

/opt/conda/envs/test4py_env/lib/python3.10/typing.py:957: TypeError
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_1.py::test_valid_input_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_1.py::test_valid_input_2
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_1.py::test_invalid_input
======================== 3 failed, 5 warnings in 0.20s =========================
"""