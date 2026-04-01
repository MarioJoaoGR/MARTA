
from dataclasses_json.core import cfg, _get_encoder_in_global_config

def test_valid_input():
    # Mock the global configuration to include an encoder for 'some_type'
    cfg.global_config.encoders['some_type'] = "mocked_encoder"
    
    # Call the function and assert that it returns the mocked encoder
    assert _get_encoder_in_global_config('some_type') == "mocked_encoder"
