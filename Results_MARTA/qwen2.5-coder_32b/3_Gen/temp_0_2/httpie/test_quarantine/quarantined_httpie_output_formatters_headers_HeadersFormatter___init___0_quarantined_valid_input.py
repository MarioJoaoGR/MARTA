
import pytest
from unittest.mock import patch
from httpie.output.formatters.headers import HeadersFormatter

def test_valid_input():
    with patch('httpie.output.formatters.headers.HeadersFormatter.format_options', {'headers': {'sort': True}}):
        formatter = HeadersFormatter()
        assert formatter.enabled is True

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_headers_HeadersFormatter___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
>       with patch('httpie.output.formatters.headers.HeadersFormatter.format_options', {'headers': {'sort': True}}):

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_headers_HeadersFormatter___init___0_test_valid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1446: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7f247d10fdd0>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <class 'httpie.output.formatters.headers.HeadersFormatter'> does not have the attribute 'format_options'

/usr/local/lib/python3.11/unittest/mock.py:1419: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_headers_HeadersFormatter___init___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.22s ===============================
"""