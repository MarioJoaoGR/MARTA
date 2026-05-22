
import pytest
from httpie.sessions import Cookie
from typing import Dict, Any

# Define the options you want to keep from the Cookie object
KEPT_COOKIE_OPTIONS = ['name', 'value', 'domain']

def materialize_cookie(cookie: Cookie) -> Dict[str, Any]:
    materialized_cookie = {
        option: getattr(cookie, option)
        for option in KEPT_COOKIE_OPTIONS
    }

    if (
        cookie._rest.get('is_explicit_none')
        and materialized_cookie['domain'] == ''
    ):
        materialized_cookie['domain'] = None

    return materialized_cookie

# Test case to check the function with valid input
def test_valid_input():
    class MockCookie(Cookie):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.name = kwargs.get('name')
            self.value = kwargs.get('value')
            self.domain = kwargs.get('domain')
            self._rest = {'is_explicit_none': False}
    
    cookie = MockCookie(name='test_cookie', value='test_value', domain='example.com')
    result = materialize_cookie(cookie)
    
    assert result['name'] == 'test_cookie'
    assert result['value'] == 'test_value'
    assert result['domain'] == 'example.com'

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

httpie/Test4DT_tests_codestral/test_httpie_sessions_materialize_cookie_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        class MockCookie(Cookie):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.name = kwargs.get('name')
                self.value = kwargs.get('value')
                self.domain = kwargs.get('domain')
                self._rest = {'is_explicit_none': False}
    
>       cookie = MockCookie(name='test_cookie', value='test_value', domain='example.com')

httpie/Test4DT_tests_codestral/test_httpie_sessions_materialize_cookie_0_test_valid_input.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'MockCookie' object has no attribute 'version'") raised in repr()] MockCookie object at 0x7fca3dca51d0>
kwargs = {'domain': 'example.com', 'name': 'test_cookie', 'value': 'test_value'}

    def __init__(self, **kwargs):
>       super().__init__(**kwargs)
E       TypeError: Cookie.__init__() missing 13 required positional arguments: 'version', 'port', 'port_specified', 'domain_specified', 'domain_initial_dot', 'path', 'path_specified', 'secure', 'expires', 'discard', 'comment', 'comment_url', and 'rest'

httpie/Test4DT_tests_codestral/test_httpie_sessions_materialize_cookie_0_test_valid_input.py:27: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_sessions_materialize_cookie_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.22s ===============================
"""