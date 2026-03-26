
import os
from isort.deprecated.finders import chdir
import pytest

def test_invalid_input():
    with pytest.raises(FileNotFoundError):
        with chdir("/nonexistent/directory"):
            pass
