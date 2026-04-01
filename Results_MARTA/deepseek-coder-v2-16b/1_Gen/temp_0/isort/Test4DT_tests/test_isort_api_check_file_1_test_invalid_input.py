
import pytest
from unittest.mock import patch
from isort.api import check_file as isort_check_file
from io import StringIO

@pytest.mark.parametrize("filename", ["nonexistentfile.py"])
def test_invalid_input(filename):
    with patch('isort.api.io.File.read', side_effect=FileNotFoundError("No such file or directory")):
        with pytest.raises(FileNotFoundError):
            isort_check_file(filename, show_diff=False)
