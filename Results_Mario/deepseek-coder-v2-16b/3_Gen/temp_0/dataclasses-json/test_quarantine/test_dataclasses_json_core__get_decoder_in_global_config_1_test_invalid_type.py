
import pytest
from your_module import _get_decoder_in_global_config  # Replace 'your_module' with the actual module name where the function resides.

@pytest.fixture(autouse=True)
def setup():
    cfg = YourConfigClass()  # Replace 'YourConfigClass' with the actual configuration class used in your code.
    cfg.global_config.decoders = {}  # Ensure there are no decoders in the global configuration.

@pytest.mark.parametrize("invalid_type", ["nonexistent_type1", "nonexistent_type2"])
def test_invalid_type(invalid_type):
    with pytest.raises(KeyError):
        _get_decoder_in_global_config(invalid_type)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_decoder_in_global_config_1_test_invalid_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_1_test_invalid_type.py:3:0: E0401: Unable to import 'your_module' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_decoder_in_global_config_1_test_invalid_type.py:7:10: E0602: Undefined variable 'YourConfigClass' (undefined-variable)


"""