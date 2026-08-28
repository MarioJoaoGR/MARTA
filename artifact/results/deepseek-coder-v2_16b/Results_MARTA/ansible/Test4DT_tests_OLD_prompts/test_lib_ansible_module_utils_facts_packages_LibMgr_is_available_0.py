
import pytest
from unittest.mock import patch, MagicMock

class LibMgr:
    LIB = None
    
    def __init__(self):
        self._lib = None
        super(LibMgr, self).__init__()

    def load_lib(self, lib):
        self._lib = lib

    def is_available(self):
        found = False
        try:
            self._lib = __import__(self.LIB)
            found = True
        except ImportError:
            pass
        return found

# Test cases
@pytest.fixture(autouse=True)
def setup():
    lib_mgr = LibMgr()
    yield lib_mgr

@pytest.mark.parametrize("lib, expected", [
    (None, False),
    ('math', True),
    ('os', True)
])
def test_is_available(setup, monkeypatch, lib, expected):
    if lib:
        with patch('builtins.__import__', return_value=MagicMock()):
            LibMgr.LIB = lib
            assert setup.is_available() == expected
