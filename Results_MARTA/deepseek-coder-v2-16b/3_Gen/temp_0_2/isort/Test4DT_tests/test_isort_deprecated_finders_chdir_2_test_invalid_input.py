
import os
from contextlib import contextmanager
import pytest

@contextmanager
def chdir(path: str):
    curdir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(curdir)

def test_invalid_input():
    with pytest.raises(FileNotFoundError):
        with chdir("nonexistent_directory"):
            assert False, "Expected a FileNotFoundError"
