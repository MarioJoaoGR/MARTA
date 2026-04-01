
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is a module with global configuration

# Mocking the necessary parts for the test
class MockConfig:
    def __init__(self):
        self.global_config = MockGlobalConfig()

class MockGlobalConfig:
    def __init__(self):
        self.decoders = ['example_decoder']  # Example decoders in global config

# Define the fixture
@pytest.fixture
def _has_decoder_in_global_config():
    return lambda type_: type_ in MockConfig().global_config.decoders

# Test case
@pytest.mark.parametrize("type_, expected", [
    ("example_decoder", True),
    ("nonexistent_decoder", False)
])
def test_invalid_input(_has_decoder_in_global_config, type_, expected):
    has_decoder = _has_decoder_in_global_config(type_)
    assert has_decoder == expected
