
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.base import ConverterPlugin

def test_valid_mime_type():
    with patch('httpie.plugins.base.ConverterPlugin', autospec=True) as mock_converter:
        converter = ConverterPlugin('application/json')
        assert converter.mime == 'application/json'
        mock_converter.assert_called_once_with('application/json')

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_base_ConverterPlugin___init___0_test_valid_mime_type.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_mime_type _____________________________

    def test_valid_mime_type():
        with patch('httpie.plugins.base.ConverterPlugin', autospec=True) as mock_converter:
            converter = ConverterPlugin('application/json')
            assert converter.mime == 'application/json'
>           mock_converter.assert_called_once_with('application/json')

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_base_ConverterPlugin___init___0_test_valid_mime_type.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='ConverterPlugin' spec='ConverterPlugin' id='139966981465936'>
args = ('application/json',), kwargs = {}
msg = "Expected 'ConverterPlugin' to be called once. Called 0 times."

    def assert_called_once_with(self, /, *args, **kwargs):
        """assert that the mock was called exactly once and that that call was
        with the specified arguments."""
        if not self.call_count == 1:
            msg = ("Expected '%s' to be called once. Called %s times.%s"
                   % (self._mock_name or 'mock',
                      self.call_count,
                      self._calls_repr()))
>           raise AssertionError(msg)
E           AssertionError: Expected 'ConverterPlugin' to be called once. Called 0 times.

/usr/local/lib/python3.11/unittest/mock.py:950: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_base_ConverterPlugin___init___0_test_valid_mime_type.py::test_valid_mime_type
============================== 1 failed in 0.11s ===============================
"""