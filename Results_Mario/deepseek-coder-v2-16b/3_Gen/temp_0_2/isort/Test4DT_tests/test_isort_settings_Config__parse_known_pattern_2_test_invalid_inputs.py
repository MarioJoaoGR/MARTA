
import pytest
from isort.settings import Config

def test_invalid_inputs():
    with pytest.raises(Exception):
        config = Config(settings_file='non_existent_file.toml', quiet=False)
