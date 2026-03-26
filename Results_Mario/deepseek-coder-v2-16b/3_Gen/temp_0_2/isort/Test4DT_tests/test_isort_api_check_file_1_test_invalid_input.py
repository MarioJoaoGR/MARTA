
import pytest
from isort.api import check_file, Config, DEFAULT_CONFIG
import io
from unittest.mock import patch

@pytest.mark.parametrize("filename", ["non_existent_file.py"])
def test_invalid_input(filename):
    with pytest.raises(FileNotFoundError):
        with patch('builtins.open', side_effect=FileNotFoundError("File not found")):
            check_file(filename)
