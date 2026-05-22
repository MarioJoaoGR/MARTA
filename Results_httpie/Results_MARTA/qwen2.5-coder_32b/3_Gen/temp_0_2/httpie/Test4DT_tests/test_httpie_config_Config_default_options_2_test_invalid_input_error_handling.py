
import pytest
from httpie.config import Config

def test_invalid_input_error_handling():
    with pytest.raises(Exception):
        config = Config()
        config['invalid_key']  # Accessing an invalid key to trigger an error
