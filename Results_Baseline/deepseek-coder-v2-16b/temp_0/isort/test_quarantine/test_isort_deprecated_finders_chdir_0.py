# Module: isort.deprecated.finders
import os
from contextlib import contextmanager
import pytest

@contextmanager
def chdir(path):
    curdir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(curdir)

# Test cases for the chdir function
def test_chdir_basic():
    with chdir('/tmp'):
        assert os.getcwd() == '/tmp'

def test_chdir_exception():
    try:
        with chdir('/nonexistent'):
            assert False, "Expected an exception"
    except FileNotFoundError:
        assert True

def test_chdir_nested():
    with chdir('/tmp'):
        with chdir('/usr'):
            assert os.getcwd() == '/usr'

def test_chdir_restore():
    original_dir = os.getcwd()
    try:
        with chdir('/tmp'):
            pass
        assert os.getcwd() == original_dir
    finally:
        os.chdir(original_dir)

def test_chdir_os_module():
    import os
    from contextlib import contextmanager

    @contextmanager
    def chdir(path):
        curdir = os.getcwd()
        os.chdir(path)
        try:
            yield
        finally:
            os.chdir(curdir)

    with chdir('/tmp'):
        assert 'os' in globals(), "The 'os' module should be available within the context"

if __name__ == "__main__":
    pytest.main()
