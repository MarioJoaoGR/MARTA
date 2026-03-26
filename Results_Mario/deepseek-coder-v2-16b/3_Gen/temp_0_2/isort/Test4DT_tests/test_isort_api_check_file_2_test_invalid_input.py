
import pytest
from isort.api import Config, check_file
import io
from unittest.mock import patch

@pytest.mark.parametrize("filename", ["non_existent_file.py"])
def test_invalid_input(filename):
    with pytest.raises(FileNotFoundError):
        check_file(filename)
