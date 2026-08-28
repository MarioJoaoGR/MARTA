
import pytest
from unittest.mock import patch, MagicMock
from httpie.client import RequestHeadersDict
from tests.httpie_test_utils import DEFAULT_UA, JSON_ACCEPT, JSON_CONTENT_TYPE, FORM_CONTENT_TYPE

@pytest.fixture(autouse=True)
def mock_default_headers():
    with patch('tests.httpie_test_utils.DEFAULT_UA', 'mocked_ua'):
        yield

@pytest.mark.parametrize("args, expected", [
    (argparse.Namespace(data=True, form=False, json=True, files=False), {'User-Agent': 'mocked_ua', 'Accept': JSON_ACCEPT, 'Content-Type': JSON_CONTENT_TYPE}),
    (argparse.Namespace(data=True, form=True, json=False, files=False), {'User-Agent': 'mocked_ua', 'Content-Type': FORM_CONTENT_TYPE}),
    (argparse.Namespace(data=True, form=False, json=True, files=True), {'User-Agent': 'mocked_ua', 'Accept': JSON_ACCEPT, 'Content-Type': JSON_CONTENT_TYPE}),
    (argparse.Namespace(data=False, form=True, json=False, files=False), {'User-Agent': 'mocked_ua', 'Content-Type': FORM_CONTENT_TYPE})
])
def test_make_default_headers(args, expected):
    headers = make_default_headers(args)
    assert headers == expected

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
________ ERROR collecting test_httpie_client_make_default_headers_0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py:5: in <module>
    from tests.httpie_test_utils import DEFAULT_UA, JSON_ACCEPT, JSON_CONTENT_TYPE, FORM_CONTENT_TYPE
E   ModuleNotFoundError: No module named 'tests.httpie_test_utils'
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 1.04s ==========================
"""