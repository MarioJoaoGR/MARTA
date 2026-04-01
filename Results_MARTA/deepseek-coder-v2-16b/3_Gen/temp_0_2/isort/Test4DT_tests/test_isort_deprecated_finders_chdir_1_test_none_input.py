
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

def test_none_input():
    with pytest.raises(TypeError):
        with chdir(None):
            pass
