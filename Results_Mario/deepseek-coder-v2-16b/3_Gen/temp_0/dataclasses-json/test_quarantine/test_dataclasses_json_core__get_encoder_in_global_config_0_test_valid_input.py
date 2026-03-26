
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is defined in your module

# Mocking the necessary parts of the configuration structure
class MockConfig:
    class MockGlobalConfig:
        class MockEncoders:
            some_type = "mocked_encoder"
        
        encoders = MockEncoders()
    
    global_config = MockGlobalConfig()

# Setting up the mock in the test environment
@pytest.fixture(autouse=True)
def setup_mocks():
    cfg.global_config.encoders = MockConfig.global_config.encoders

# Test case for _get_encoder_in_global_config function
def test_valid_input():
    from dataclasses_json.core import _get_encoder_in_global_config
    
    # Act
    encoder = _get_encoder_in_global_config('some_type')
    
    # Assert
    assert encoder == "mocked_encoder"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        from dataclasses_json.core import _get_encoder_in_global_config
    
        # Act
>       encoder = _get_encoder_in_global_config('some_type')

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_0_test_valid_input.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = 'some_type'

    def _get_encoder_in_global_config(type_):
>       return cfg.global_config.encoders[type_]
E       TypeError: 'MockEncoders' object is not subscriptable

dataclasses-json/dataclasses_json/core.py:475: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""