
import pytest
from dataclasses_json.core import _get_decoder_in_global_config

# Assuming cfg is a module or class containing the global configuration
class MockCfg:
    global_config = {
        'decoders': {
            'json': "JSONDecoder",
            'xml': "XMLDecoder",
            'custom_type': "CustomTypeDecoder"
        }
    }

def test_get_decoder_in_global_config_valid_type():
    cfg = MockCfg()
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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0.py F [100%]

=================================== FAILURES ===================================
_________________ test_get_decoder_in_global_config_valid_type _________________

    def test_get_decoder_in_global_config_valid_type():
        cfg = MockCfg()
>       assert _get_decoder_in_global_config('json') == "JSONDecoder"

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = 'json'

    def _get_decoder_in_global_config(type_):
>       return cfg.global_config.decoders[type_]
E       KeyError: 'json'

dataclasses-json/dataclasses_json/core.py:467: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0.py::test_get_decoder_in_global_config_valid_type
============================== 1 failed in 0.03s ===============================

"""