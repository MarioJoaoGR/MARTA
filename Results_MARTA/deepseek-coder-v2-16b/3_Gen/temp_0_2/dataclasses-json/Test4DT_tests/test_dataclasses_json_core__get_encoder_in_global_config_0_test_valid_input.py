
import pytest
from dataclasses_json.core import cfg  # Assuming this is the module you are importing from

# Mocking the global configuration dictionary
class MockConfig:
    encoders = {
        'some_type': "MockEncoder"
    }

@pytest.fixture(autouse=True)
def setup_mock():
    cfg.global_config = MockConfig()

def test_valid_input():
    from dataclasses_json.core import _get_encoder_in_global_config
    
    # Test retrieving an existing encoder type
    assert _get_encoder_in_global_config('some_type') == "MockEncoder"
    
    # Test with a non-existing type to ensure it raises KeyError if the key is not found
    with pytest.raises(KeyError):
        _get_encoder_in_global_config('non_existent_type')
