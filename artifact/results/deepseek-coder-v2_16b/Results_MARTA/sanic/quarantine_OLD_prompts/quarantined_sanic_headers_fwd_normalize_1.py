
import pytest
from unittest.mock import patch
from typing import Dict, Union, OptionsIterable
from urllib.parse import unquote
from sanic.headers import fwd_normalize

def test_fwd_normalize_basic():
    with patch('sanic.headers.unquote', return_value='foo/bar'):
        result = fwd_normalize({'by': 'Example Corp', 'host': 'example.com', 'port': '8080', 'path': 'foo%2Bar'})
        assert result == {'by': 'Example Corp', 'host': 'example.com', 'port': 8080, 'path': 'foo/bar'}

def test_fwd_normalize_protocols():
    with patch('sanic.headers.unquote', return_value='baz/qux'):
        result = fwd_normalize({'proto': 'HTTP/1.1', 'for': '[2001:db8::1]'})
        assert result == {'proto': 'http', 'for': '[2001:db8::1]'}

def test_fwd_normalize_mixed():
    with patch('sanic.headers.unquote', return_value='baz/qux'):
        result = fwd_normalize({'by': 'Another Corp', 'host': 'EXAMPLE.COM', 'port': '9090', 'path': 'baz%2Fqux'})
        assert result == {'by': 'Another Corp', 'host': 'example.com', 'port': 9090, 'path': 'baz/qux'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
____________ ERROR collecting test_sanic_headers_fwd_normalize_1.py ____________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_1.py:4: in <module>
    from typing import Dict, Union, OptionsIterable
E   ImportError: cannot import name 'OptionsIterable' from 'typing' (/opt/conda/envs/test4py_env/lib/python3.10/typing.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""