
import pytest
from httpie.config import Config

def test_invalid_input_error_handling():
    with pytest.raises(Exception):
        config = Config()
        config['invalid_key']  # This should raise an Exception due to invalid key access
