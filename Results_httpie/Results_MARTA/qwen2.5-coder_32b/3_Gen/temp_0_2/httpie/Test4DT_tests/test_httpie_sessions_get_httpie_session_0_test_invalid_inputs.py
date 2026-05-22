
import pytest
from httpie.sessions import Environment, get_httpie_session
from pathlib import Path
from unittest.mock import patch

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case for invalid inputs
        env = Environment()
        config_dir = Path('~/.httpie').expanduser()
        get_httpie_session(env, config_dir, 12345, "host", "url")
