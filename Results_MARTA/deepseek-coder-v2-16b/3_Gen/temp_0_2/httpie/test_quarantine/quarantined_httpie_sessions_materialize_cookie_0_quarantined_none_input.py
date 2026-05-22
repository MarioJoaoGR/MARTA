
import pytest
from httpie.sessions import materialize_cookie, Cookie

def test_none_input():
    cookie = None
    with pytest.raises(TypeError):
        materialize_cookie(cookie)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_materialize_cookie_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        cookie = None
        with pytest.raises(TypeError):
>           materialize_cookie(cookie)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_materialize_cookie_0_test_none_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/sessions.py:61: in materialize_cookie
    materialized_cookie = {
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x7f5b7d128c40>

    materialized_cookie = {
>       option: getattr(cookie, option)
        for option in KEPT_COOKIE_OPTIONS
    }
E   AttributeError: 'NoneType' object has no attribute 'name'

httpie/httpie/sessions.py:62: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_materialize_cookie_0_test_none_input.py::test_none_input
============================== 1 failed in 0.24s ===============================
"""