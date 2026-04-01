
import pytest
from dataclasses_json.core import cfg  # Assuming this is the module where cfg is defined

# Mocking the necessary parts of the system under test
class MockEncoder:
    pass

class MockGlobalConfig:
    def __init__(self):
        self.encoders = {}

@pytest.fixture(autouse=True)
def setup_mock():
    # Setup the mock configuration
    cfg.global_config = MockGlobalConfig()
    cfg.global_config.encoders['some_type'] = MockEncoder()

def test_valid_input():
    from dataclasses_json.core import _get_encoder_in_global_config as get_encoder
    
    # Act
    encoder = get_encoder('some_type')
    
    # Assert
    assert isinstance(encoder, MockEncoder)
