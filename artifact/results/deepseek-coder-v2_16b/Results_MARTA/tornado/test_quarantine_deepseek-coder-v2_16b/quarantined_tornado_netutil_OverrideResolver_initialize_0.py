
import pytest
from tornado.netutil import OverrideResolver
from dns import Resolver
import socket

class TestOverrideResolver:
    def setup_method(self, method):
        self.resolver = Resolver()
        self.overrides = {
            "example.com": "127.0.0.1",
            ("login.example.com", 443): ("localhost", 1443),
            ("login.example.com", 443, socket.AF_INET6): ("::1", 1443)
        }
        self.override_resolver = OverrideResolver(resolver=self.resolver, mapping=self.overrides)

    def test_initialize(self):
        assert isinstance(self.override_resolver.resolver, Resolver)
        assert self.override_resolver.mapping == {
            "example.com": "127.0.0.1",
            ("login.example.com", 443): ("localhost", 1443),
            ("login.example.com", 443, socket.AF_INET6): ("::1", 1443)
        }

    def test_resolve(self):
        resolved_ips = self.override_resolver.resolve("example.com", 80)
        assert "127.0.0.1" in resolved_ips

if __name__ == "__main__":
    pytest.main()

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
____ ERROR collecting test_tornado_netutil_OverrideResolver_initialize_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_OverrideResolver_initialize_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_OverrideResolver_initialize_0.py:4: in <module>
    from dns import Resolver
E   ModuleNotFoundError: No module named 'dns'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_netutil_OverrideResolver_initialize_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""