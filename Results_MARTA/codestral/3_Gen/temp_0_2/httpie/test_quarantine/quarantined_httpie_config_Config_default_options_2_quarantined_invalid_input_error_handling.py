
import pytest
from httpie.config import Config

def test_invalid_input_error_handling():
    with pytest.raises(Exception):
        config = Config()  # Initialize a new Config instance without providing a directory, which should raise an Exception

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

httpie/Test4DT_tests_codestral/test_httpie_config_Config_default_options_2_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

httpie/Test4DT_tests_codestral/test_httpie_config_Config_default_options_2_test_invalid_input_error_handling.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_config_Config_default_options_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling
============================== 1 failed in 0.16s ===============================
"""