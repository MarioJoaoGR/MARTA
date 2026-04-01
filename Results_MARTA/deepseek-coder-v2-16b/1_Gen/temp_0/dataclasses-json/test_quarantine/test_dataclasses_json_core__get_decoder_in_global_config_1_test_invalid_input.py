
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is defined in the core module

# Mocking the necessary parts of the global configuration
class MockGlobalConfig:
    def __init__(self):
        self.decoders = {
            'some_type': lambda x: None  # Example decoder function
        }

def test_invalid_input():
    with pytest.raises(KeyError):
        from dataclasses_json.core import _get_decoder_in_global_config
        
        # Mocking the global configuration to return a mock object
        cfg.global_config = MockGlobalConfig()
        
        # Providing an invalid type that should raise KeyError
        with pytest.raises(KeyError):
            _get_decoder_in_global_config('invalid_type')

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_1_test_invalid_input.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================

"""