
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is part of the module 'dataclasses_json.core'

# Mocking the necessary parts for the test
class GlobalConfigMock:
    def __init__(self):
        self.decoders = {
            'some_type': "mocked_decoder"
        }

@pytest.fixture(autouse=True)
def setup():
    # Set up the mock configuration
    cfg.global_config = GlobalConfigMock()

# Test case for _get_decoder_in_global_config function
def test_valid_input():
    from dataclasses_json.core import _get_decoder_in_global_config
    
    # Call the function with a valid type
    decoder = _get_decoder_in_global_config('some_type')
    
    # Assert that the returned decoder is correct
    assert decoder == "mocked_decoder"
