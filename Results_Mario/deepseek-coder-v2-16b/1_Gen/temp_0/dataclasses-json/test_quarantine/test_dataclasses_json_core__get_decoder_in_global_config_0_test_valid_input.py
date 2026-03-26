
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is defined in the core module

# Mocking the global configuration and its decoders
@pytest.fixture(autouse=True)
def mock_global_config():
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(cfg, 'global_config', {
            'decoders': {
                'some_type': lambda x: f"Decoded {x}"  # Mock decoder function
            }
        })
        yield

def test_valid_input():
    from dataclasses_json.core import _get_decoder_in_global_config
    
    result = _get_decoder_in_global_config('some_type')
    assert result == "Decoded some_type"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        from dataclasses_json.core import _get_decoder_in_global_config
    
>       result = _get_decoder_in_global_config('some_type')

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0_test_valid_input.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = 'some_type'

    def _get_decoder_in_global_config(type_):
>       return cfg.global_config.decoders[type_]
E       AttributeError: 'dict' object has no attribute 'decoders'

dataclasses-json/dataclasses_json/core.py:467: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================

"""