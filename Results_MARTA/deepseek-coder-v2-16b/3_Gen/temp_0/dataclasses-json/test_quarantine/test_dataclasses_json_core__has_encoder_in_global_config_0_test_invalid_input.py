
import pytest
from dataclasses_json.core import cfg  # Assuming this is the correct module and variable name

def _has_encoder_in_global_config(type_):
    return type_ in cfg.global_config.encoders

def test_invalid_input():
    with pytest.raises(TypeError):
        _has_encoder_in_global_config(123)  # Providing an invalid input type (int) to trigger TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_invalid_input.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""