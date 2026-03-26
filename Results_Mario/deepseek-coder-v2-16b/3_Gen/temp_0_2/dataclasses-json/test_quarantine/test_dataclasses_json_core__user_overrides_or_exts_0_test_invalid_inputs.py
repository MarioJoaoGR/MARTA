
from dataclasses import fields
from collections import defaultdict
import pytest
from dataclasses_json.core import _user_overrides_or_exts

# Assuming cfg is a module or object containing global configurations for encoders, decoders, and mm_fields
class MockConfig:
    def __init__(self):
        self.global_config = MockGlobalConfig()

class MockGlobalConfig:
    def __init__(self):
        self.encoders = {}
        self.decoders = {}
        self.mm_fields = {}

@pytest.fixture
def mock_config():
    return MockConfig()

# Define a dataclass for testing
from dataclasses import dataclass

@dataclass
class MyDataClass:
    name: str
    age: int
    address: str = "123 Main St"

def test_invalid_inputs(mock_config):
    # Test the function with an invalid input, such as a non-dataclass type
    class InvalidType:
        pass
    
    with pytest.raises(TypeError):
        _user_overrides_or_exts(InvalidType)
