
import pytest
from dataclasses_json.cfg import _GlobalConfig

# Test for registering and getting an encoder

# Test for registering and getting a decoder

# Test for handling invalid input
def test_invalid_input():
    config = _GlobalConfig()
    
    with pytest.raises(AttributeError):
        config._GlobalConfig__init__()