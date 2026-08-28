
import pytest
from httpie.client import RequestHeadersDict
from test_httpie_client_finalize_headers_0 import finalize_headers  # Assuming the function is in a module named test_httpie_client_finalize_headers_0

def test_finalize_headers_non_string():
    headers = RequestHeadersDict({'Content-Type': 'application/json', 'User-Agent': 123})
    result = finalize_headers(headers)
    assert result == {'Content-Type': b'application/json', 'User-Agent': 123}

def test_finalize_headers_whitespace():
    headers = RequestHeadersDict({'Content-Type': ' application/json ', 'User-Agent': ' httpie '})
    result = finalize_headers(headers)
    assert result == {'Content-Type': b'application/json', 'User-Agent': b'httpie'}

def test_finalize_headers_empty():
    headers = RequestHeadersDict({})
    result = finalize_headers(headers)
    assert result == {}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__________ ERROR collecting test_httpie_client_finalize_headers_0.py ___________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_finalize_headers_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_finalize_headers_0.py:4: in <module>
    from test_httpie_client_finalize_headers_0 import finalize_headers  # Assuming the function is in a module named test_httpie_client_finalize_headers_0
E   ImportError: cannot import name 'finalize_headers' from partially initialized module 'test_httpie_client_finalize_headers_0' (most likely due to a circular import) (/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_finalize_headers_0.py)
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_finalize_headers_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 1.17s ==========================
"""