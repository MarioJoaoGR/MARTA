
import pytest
from isort import Config

def test_valid_inputs():
    # Test valid inputs for Config class
    with pytest.raises(TypeError):
        config = Config(config={"sections": ["known_standard_library", "known_future_library"]})
