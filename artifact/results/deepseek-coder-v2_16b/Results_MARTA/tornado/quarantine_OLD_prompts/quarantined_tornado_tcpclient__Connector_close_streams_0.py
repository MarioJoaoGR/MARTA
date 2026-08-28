
import pytest
from tornado.tcpclient import _Connector, IOLoop
from tornado.concurrent import Future
from unittest.mock import patch, MagicMock
import socket
from typing import List, Tuple, IOStream

@pytest.fixture(scope="module")
def connector():
    def connect_func(af, addr):
        sock = socket.socket(af, socket.SOCK_STREAM)
        stream = IOStream(sock)
        future = Future()
        return (stream, future)

    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80)), (socket.AF_INET6, ('::1', 80))]
    connector = _Connector(addrinfo, connect_func)
    return connector

def test_connector_initialization(connector):
    assert isinstance(connector.io_loop, IOLoop)
    assert len(connector.primary_addrs) == 1
    assert len(connector.secondary_addrs) == 1
    assert all(isinstance(addr, tuple) for addr in connector.primary_addrs)
    assert all(isinstance(addr, tuple) for addr in connector.secondary_addrs)

def test_connector_close_streams(connector):
    with patch('tornado.tcpclient._Connector.IOStream', new=MagicMock()) as mock_stream:
        connector.streams.add(mock_stream)
        connector.close_streams()
        assert mock_stream.close.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
____ ERROR collecting test_tornado_tcpclient__Connector_close_streams_0.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_tcpclient__Connector_close_streams_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_tcpclient__Connector_close_streams_0.py:7: in <module>
    from typing import List, Tuple, IOStream
E   ImportError: cannot import name 'IOStream' from 'typing' (/opt/conda/envs/test4py_env/lib/python3.10/typing.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_tcpclient__Connector_close_streams_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.18s ===============================
"""