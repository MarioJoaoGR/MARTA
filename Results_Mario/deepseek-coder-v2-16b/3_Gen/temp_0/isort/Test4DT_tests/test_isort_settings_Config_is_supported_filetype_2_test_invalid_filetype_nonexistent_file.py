
import pytest
from unittest.mock import patch
from isort.settings import Config  # Assuming this is the correct module to import from

@pytest.mark.parametrize("file_name", ["test.py", "test.txt", "test.log", "test.bak"])
def test_is_supported_filetype(file_name):
    with patch('isort.settings.os.path.splitext', return_value=('', '')):
        config = Config()
        assert not config.is_supported_filetype(file_name)
