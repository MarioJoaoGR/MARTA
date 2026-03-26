
import os
from contextlib import contextmanager
from isort.deprecated.finders import chdir
import pytest

@pytest.fixture
def invalid_path():
    return "/invalid/path"

def test_invalid_path(invalid_path):
    with pytest.raises(FileNotFoundError):
        with chdir(invalid_path) as cm:
            pass
