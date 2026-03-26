
# Module: dataclasses_json.core
# Import the function correctly using its module name
from dataclasses_json.core import _has_encoder_in_global_config as has_encoder
import pytest

# Test cases for _has_encoder_in_global_config
def test_has_encoder_found():
    # Arrange: Set up the global configuration to include an encoder for 'example_encoder'
    from dataclasses_json import cfg  # Importing here to avoid undefined variable error
    cfg.global_config.encoders = {'example_encoder': None}
    
    # Act: Call the function with 'example_encoder'
    result = has_encoder('example_encoder')
    
    # Assert: Check that the result is True
    assert result == True, "Expected to find an encoder for 'example_encoder'"

def test_has_encoder_not_found():
    # Arrange: Set up the global configuration without any encoders
    from dataclasses_json import cfg  # Importing here to avoid undefined variable error
    cfg.global_config.encoders = {}
    
    # Act: Call the function with a type that is not in the global config
    result = has_encoder('non_existent_encoder')
    
    # Assert: Check that the result is False
    assert result == False, "Expected to not find an encoder for 'non_existent_encoder'"

def test_has_encoder_with_none():
    # Arrange: Set up the global configuration without any encoders
    from dataclasses_json import cfg  # Importing here to avoid undefined variable error
    cfg.global_config.encoders = {}
    
    # Act: Call the function with None
    result = has_encoder(None)
    
    # Assert: Check that the result is False, as there should be no default encoder for None
    assert result == False, "Expected to not find a default encoder for None"

def test_has_encoder_with_int():
    # Arrange: Set up the global configuration without any encoders
    from dataclasses_json import cfg  # Importing here to avoid undefined variable error
    cfg.global_config.encoders = {}
    
    # Act: Call the function with int type
    result = has_encoder(int)
    
    # Assert: Check that the result is False, as there should be no default encoder for int
    assert result == False, "Expected to not find a default encoder for int"
