
import pytest
from tornado.netutil import TCPClient, Resolver

def test_tcpclient_default_resolver():
    client = TCPClient()
    assert isinstance(client.resolver, Resolver)
    assert not hasattr(client, '_own_resolver')  # Ensure _own_resolver is not directly accessible

def test_tcpclient_custom_resolver():
    custom_resolver = Resolver()
    client = TCPClient(resolver=custom_resolver)
    assert client.resolver == custom_resolver
    assert not client._own_resolver  # Ensure _own_resolver is not set by the constructor

def test_tcpclient_no_resolver():
    client = TCPClient()
    assert isinstance(client.resolver, Resolver)
    assert not hasattr(client, '_own_resolver')  # Ensure _own_resolver is not directly accessible

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
_______ ERROR collecting test_tornado_tcpclient_TCPClient___init___0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_tcpclient_TCPClient___init___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_tcpclient_TCPClient___init___0.py:3: in <module>
    from tornado.netutil import TCPClient, Resolver
E   ImportError: cannot import name 'TCPClient' from 'tornado.netutil' (/opt/marta/baselines/codamosa/replication/test-apps/tornado/tornado/netutil.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_tcpclient_TCPClient___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""