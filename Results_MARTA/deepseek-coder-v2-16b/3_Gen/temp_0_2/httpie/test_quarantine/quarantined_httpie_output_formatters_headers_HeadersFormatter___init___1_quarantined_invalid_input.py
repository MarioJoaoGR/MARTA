
import pytest
from httpie.output.formatters.headers import HeadersFormatter

def test_invalid_input():
    with pytest.raises(TypeError):
        HeadersFormatter()

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_headers_HeadersFormatter___init___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
>           HeadersFormatter()

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_headers_HeadersFormatter___init___1_test_invalid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/output/formatters/headers.py:7: in __init__
    super().__init__(**kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.formatters.headers.HeadersFormatter object at 0x7f635b6c9310>
kwargs = {}

    def __init__(self, **kwargs):
        """
        :param env: an class:`Environment` instance
        :param kwargs: additional keyword argument that some
                       formatters might require.
    
        """
        self.enabled = True
        self.kwargs = kwargs
>       self.format_options = kwargs['format_options']
E       KeyError: 'format_options'

httpie/httpie/plugins/base.py:140: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_headers_HeadersFormatter___init___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""