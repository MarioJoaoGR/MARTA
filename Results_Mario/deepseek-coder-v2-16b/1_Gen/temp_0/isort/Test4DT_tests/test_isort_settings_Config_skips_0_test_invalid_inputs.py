
import pytest
from isort.settings import Config  # Import from the correct module

def test_invalid_inputs():
    with pytest.raises(FileNotFoundError):
        config = Config(settings_file="non_existent_file.ini")
