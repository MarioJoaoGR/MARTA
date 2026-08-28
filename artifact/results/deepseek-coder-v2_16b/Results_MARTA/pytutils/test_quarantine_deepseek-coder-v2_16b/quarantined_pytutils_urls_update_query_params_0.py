
import pytest
from pytutils.urls import update_query_params
from urllib.parse import urlparse, parse_qs, urlunsplit, urlencode


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_urls_update_query_params_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_edge_case_none_values __________________________

    def test_edge_case_none_values():
        url = 'http://example.com?foo=bar&biz=baz'
        params = {'new_param': None}
        expected_output = 'http://example.com?foo=bar&biz=baz&new_param='
>       assert update_query_params(url, params) == expected_output
E       AssertionError: assert 'http://examp...ew_param=None' == 'http://examp...az&new_param='
E         
E         Skipping 34 identical leading characters in diff, use -v to show
E         - &new_param=
E         + &new_param=None
E         ?            ++++

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_urls_update_query_params_0.py:10: AssertionError
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        url = 'invalid-url'
        params = {'foo': 'stuff'}
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_urls_update_query_params_0.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_urls_update_query_params_0.py::test_edge_case_none_values
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_urls_update_query_params_0.py::test_invalid_input_error_handling
============================== 2 failed in 0.05s ===============================
"""