
import pytest

from isort.exceptions import FileSkipped


def test_invalid_inputs():
    with pytest.raises(FileSkipped):
        raise FileSkipped("Invalid input", "non/existent/file.txt")
