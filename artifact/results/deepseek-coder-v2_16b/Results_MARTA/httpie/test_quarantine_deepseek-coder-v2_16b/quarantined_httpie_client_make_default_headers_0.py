
import pytest
from httpie.client import make_default_headers
import argparse




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_____________________ test_make_default_headers_with_json ______________________

    def test_make_default_headers_with_json():
        args = argparse.Namespace(data=True, form=False, json=True, files=False)
        headers = make_default_headers(args)
>       assert headers == {'User-Agent': 'DEFAULT_UA', 'Accept': 'JSON_ACCEPT', 'Content-Type': 'application/json'}
E       AssertionError: assert {'User-Agent'...ication/json'} == {'Accept': 'J... 'DEFAULT_UA'}
E         
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py:9: AssertionError
_____________________ test_make_default_headers_with_form ______________________

    def test_make_default_headers_with_form():
        args = argparse.Namespace(data=True, form=True, json=False, files=False)
        headers = make_default_headers(args)
>       assert headers == {'User-Agent': 'DEFAULT_UA', 'Content-Type': 'FORM_CONTENT_TYPE'}
E       AssertionError: assert {'User-Agent'...harset=utf-8'} == {'Content-Typ... 'DEFAULT_UA'}
E         
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py:14: AssertionError
________________ test_make_default_headers_with_json_and_files _________________

    def test_make_default_headers_with_json_and_files():
        args = argparse.Namespace(data=True, form=False, json=True, files=True)
        headers = make_default_headers(args)
>       assert headers == {'User-Agent': 'DEFAULT_UA', 'Accept': 'JSON_ACCEPT', 'Content-Type': 'application/json'}
E       AssertionError: assert {'User-Agent'...ication/json'} == {'Accept': 'J... 'DEFAULT_UA'}
E         
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py:19: AssertionError
_________________ test_make_default_headers_with_form_no_files _________________

    def test_make_default_headers_with_form_no_files():
        args = argparse.Namespace(data=False, form=True, json=False, files=False)
        headers = make_default_headers(args)
>       assert headers == {'User-Agent': 'DEFAULT_UA', 'Content-Type': 'FORM_CONTENT_TYPE'}
E       AssertionError: assert {'User-Agent'...harset=utf-8'} == {'Content-Typ... 'DEFAULT_UA'}
E         
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py:24: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py::test_make_default_headers_with_json
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py::test_make_default_headers_with_form
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py::test_make_default_headers_with_json_and_files
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_client_make_default_headers_0.py::test_make_default_headers_with_form_no_files
========================= 4 failed, 1 warning in 0.44s =========================
"""