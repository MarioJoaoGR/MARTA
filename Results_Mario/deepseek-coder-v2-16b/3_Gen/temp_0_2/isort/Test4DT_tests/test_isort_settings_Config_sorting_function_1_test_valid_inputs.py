
import pytest
from isort.settings import Config

def test_valid_inputs():
    with pytest.raises(FileNotFoundError):
        config = Config(settings_file='path/to/config.ini', quiet=True)
