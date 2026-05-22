
import pytest
from httpie.config import Config

def test_invalid_input_error_handling():
    with pytest.raises(Exception):
        config = Config()
        # Attempt to access a non-existent key, which should raise an Exception
        config['non_existent_key']
