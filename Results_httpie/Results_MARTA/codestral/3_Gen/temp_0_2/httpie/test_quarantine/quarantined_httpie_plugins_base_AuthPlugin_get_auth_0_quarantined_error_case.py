
import requests.auth
from httpie.plugins.base import AuthPlugin

class TestAuthPlugin(AuthPlugin):
    def get_auth(self, username: str = None, password: str = None):
        if self.auth_parse and username is not None and password is not None:
            return requests.auth.HTTPBasicAuth(username, password)
        raise NotImplementedError()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
============================ no tests ran in 0.10s =============================
"""