
import pytest
from httpie.output.formatters.json import JSONFormatter


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_json_JSONFormatter___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        with pytest.raises(KeyError):
>           formatter = JSONFormatter(format_options=None)

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_json_JSONFormatter___init___0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.formatters.json.JSONFormatter object at 0x7fc83889cc70>
kwargs = {'format_options': None}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
>       self.enabled = self.format_options['json']['format']
E       TypeError: 'NoneType' object is not subscriptable

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/output/formatters/json.py:11: TypeError
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        with pytest.raises(KeyError):
>           formatter = JSONFormatter(format_options={'json': 'invalid'})

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_json_JSONFormatter___init___0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.formatters.json.JSONFormatter object at 0x7fc83889d600>
kwargs = {'format_options': {'json': 'invalid'}}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
>       self.enabled = self.format_options['json']['format']
E       TypeError: string indices must be integers

/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/output/formatters/json.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_json_JSONFormatter___init___0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_json_JSONFormatter___init___0.py::test_invalid_input_error_handling
============================== 2 failed in 0.07s ===============================
"""