
import pytest
from httpie.plugins.base import ConverterPlugin

class TestConverterPluginSupports(object):
    @classmethod
    def setup_class(cls):
        cls.converter = ConverterPlugin("application/custom-mime")

    def test_supports_invalid_mime(self):
        """Test that supports returns False for an invalid MIME type."""
        assert not self.converter.supports("application/invalid-mime")

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

httpie/Test4DT_tests_codestral/test_httpie_plugins_base_ConverterPlugin_supports_5_test_valid_input.py F [100%]

=================================== FAILURES ===================================
____________ TestConverterPluginSupports.test_supports_invalid_mime ____________

self = <Test4DT_tests_codestral.test_httpie_plugins_base_ConverterPlugin_supports_5_test_valid_input.TestConverterPluginSupports object at 0x7f1820c5bbd0>

    def test_supports_invalid_mime(self):
        """Test that supports returns False for an invalid MIME type."""
>       assert not self.converter.supports("application/invalid-mime")

httpie/Test4DT_tests_codestral/test_httpie_plugins_base_ConverterPlugin_supports_5_test_valid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'httpie.plugins.base.ConverterPlugin'>
mime = 'application/invalid-mime'

    @classmethod
    def supports(cls, mime: str) -> bool:
>       raise NotImplementedError
E       NotImplementedError

httpie/httpie/plugins/base.py:121: NotImplementedError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_plugins_base_ConverterPlugin_supports_5_test_valid_input.py::TestConverterPluginSupports::test_supports_invalid_mime
============================== 1 failed in 0.13s ===============================
"""