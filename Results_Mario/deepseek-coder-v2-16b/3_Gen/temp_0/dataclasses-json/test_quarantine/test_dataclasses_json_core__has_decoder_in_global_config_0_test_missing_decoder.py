
import pytest
from dataclasses_json import core as cfg

@pytest.mark.skip(reason="Ensure cfg.global_config.decoders does not contain 'non_existent_decoder'")
def test_missing_decoder():
    # Ensure the decoder type is not present in the global configuration
    assert 'non_existent_decoder' not in cfg.global_config.decoders

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_0_test_missing_decoder
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_missing_decoder.py:8:41: E1101: Module 'dataclasses_json.core' has no 'global_config' member (no-member)


"""