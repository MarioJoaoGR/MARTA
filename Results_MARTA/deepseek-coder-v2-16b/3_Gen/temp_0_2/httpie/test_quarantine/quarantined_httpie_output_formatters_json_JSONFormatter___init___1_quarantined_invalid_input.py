
import pytest
from httpie.output.formatters.json import JSONFormatter

def test_invalid_input():
    with pytest.raises(KeyError):
        formatter = JSONFormatter(format_options='incorrect_type')

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_json_JSONFormatter___init___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(KeyError):
>           formatter = JSONFormatter(format_options='incorrect_type')

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_json_JSONFormatter___init___1_test_invalid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.formatters.json.JSONFormatter object at 0x7f727c6f9d90>
kwargs = {'format_options': 'incorrect_type'}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
>       self.enabled = self.format_options['json']['format']
E       TypeError: string indices must be integers, not 'str'

httpie/httpie/output/formatters/json.py:10: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_json_JSONFormatter___init___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.16s ===============================
"""