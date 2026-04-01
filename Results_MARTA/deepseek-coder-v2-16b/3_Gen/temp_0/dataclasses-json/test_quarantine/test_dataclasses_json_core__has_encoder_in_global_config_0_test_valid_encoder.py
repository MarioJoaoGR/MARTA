
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is defined in this module

def _has_encoder_in_global_config(type_):
    return type_ in cfg.global_config.encoders

def test_valid_encoder():
    assert _has_encoder_in_global_config('example_encoder') == True

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_valid_encoder.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_encoder ______________________________

    def test_valid_encoder():
>       assert _has_encoder_in_global_config('example_encoder') == True
E       AssertionError: assert False == True
E        +  where False = _has_encoder_in_global_config('example_encoder')

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_valid_encoder.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_encoder_in_global_config_0_test_valid_encoder.py::test_valid_encoder
============================== 1 failed in 0.03s ===============================
"""