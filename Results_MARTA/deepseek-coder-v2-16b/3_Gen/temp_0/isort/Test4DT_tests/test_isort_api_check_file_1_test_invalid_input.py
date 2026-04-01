
from io import StringIO
from unittest.mock import patch

import pytest

from isort.api import check_file as isort_check_file


@pytest.mark.parametrize("filename", ["nonexistentfile.py"])
def test_invalid_input(filename):
    with patch('isort.api.io.File.read', side_effect=FileNotFoundError("No such file or directory")):
        with pytest.raises(FileNotFoundError):
            isort_check_file(filename, show_diff=False)
