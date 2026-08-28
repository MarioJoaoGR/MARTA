
import pytest
from socksocket import sockssocket, ProxyType

def test_sockssocket_set_up_socks5_proxy():
    sock = sockssocket()
    sock.setproxy(ProxyType.SOCKS5, '127.0.0.1', 9050)
    assert sock._proxy is not None
    assert sock._proxy['type'] == ProxyType.SOCKS5
    assert sock._proxy['host'] == '127.0.0.1'
    assert sock._proxy['port'] == 9050

def test_sockssocket_connect_via_socks5_proxy():
    sock = sockssocket()
    sock.setproxy(ProxyType.SOCKS5, '127.0.0.1', 9050)
    with pytest.raises(Exception):
        sock.connect(('8.8.8.8', 53))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
____ ERROR collecting test_youtube_dl_socks_sockssocket__setup_socks5_0.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_sockssocket__setup_socks5_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_sockssocket__setup_socks5_0.py:3: in <module>
    from socksocket import sockssocket, ProxyType
E   ModuleNotFoundError: No module named 'socksocket'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_sockssocket__setup_socks5_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""