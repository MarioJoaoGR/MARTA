
import pytest
from tornado.auth import OAuth2Mixin
from urllib.parse import url_concat

class TestOAuth2Mixin:
    def setup_method(self):
        self.mixin = OAuth2Mixin()
        self.mixin._OAUTH_ACCESS_TOKEN_URL = "https://auth-server.com/token"

    @pytest.mark.parametrize("redirect_uri, client_id, expected", [
        ("https://example.com/callback", "client123", "https://auth-server.com/token?redirect_uri=https%3A//example.com/callback&client_id=client123"),
        (None, "client123", "https://auth-server.com/token?client_id=client123"),
    ])
    def test_oauth_request_token_url(self, redirect_uri, client_id, expected):
        result = self.mixin._oauth_request_token_url(redirect_uri=redirect_uri, client_id=client_id)
        assert url_concat("https://auth-server.com/token", {"redirect_uri": redirect_uri, "client_id": client_id}) == expected

    @pytest.mark.parametrize("code, expected", [
        ("auth_code789", "https://auth-server.com/token?client_id=client123&code=auth_code789"),
        (None, "https://auth-server.com/token?client_id=client123"),
    ])
    def test_oauth_request_token_url_with_code(self, code, expected):
        result = self.mixin._oauth_request_token_url(client_id="client123", code=code)
        assert url_concat("https://auth-server.com/token", {"client_id": "client123", "code": code}) == expected

    @pytest.mark.parametrize("extra_params, expected", [
        ({"state": "abc123"}, "https://auth-server.com/token?client_id=client123&state=abc123"),
        ({}, "https://auth-server.com/token?client_id=client123"),
    ])
    def test_oauth_request_token_url_with_extra_params(self, extra_params, expected):
        result = self.mixin._oauth_request_token_url(client_id="client123", extra_params=extra_params)
        assert url_concat("https://auth-server.com/token", {"client_id": "client123", **extra_params}) == expected

    @pytest.mark.parametrize("client_secret, expected", [
        ("secret456", "https://auth-server.com/token?client_id=client123&client_secret=secret456"),
        (None, "https://auth-server.com/token?client_id=client123"),
    ])
    def test_oauth_request_token_url_with_client_secret(self, client_secret, expected):
        result = self.mixin._oauth_request_token_url(client_id="client123", client_secret=client_secret)
        assert url_concat("https://auth-server.com/token", {"client_id": "client123", "client_secret": client_secret}) == expected

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
_ ERROR collecting test_tornado_auth_OAuth2Mixin__oauth_request_token_url_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth_OAuth2Mixin__oauth_request_token_url_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth_OAuth2Mixin__oauth_request_token_url_0.py:4: in <module>
    from urllib.parse import url_concat
E   ImportError: cannot import name 'url_concat' from 'urllib.parse' (/opt/conda/envs/test4py_env/lib/python3.10/urllib/parse.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth_OAuth2Mixin__oauth_request_token_url_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.20s ===============================
"""