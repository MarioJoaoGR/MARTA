
import pytest
from unittest.mock import patch

class LibMgr:
    LIB = None
    
    def __init__(self):
        self._lib = None
        super(LibMgr, self).__init__()

    def is_available(self):
        found = False
        try:
            self._lib = __import__(self.LIB)
            found = True
        except ImportError:
            pass
        return found

# Test cases
def test_valid_case():
    with patch('builtins.__import__', return_value=True):
        lib_mgr = LibMgr()
        LibMgr.LIB = 'math'
        assert lib_mgr.is_available() == True

def test_missing_lib_case():
    lib_mgr = LibMgr()
    assert lib_mgr.is_available() == False

def test_error_case():
    with patch('builtins.__import__', side_effect=ImportError):
        lib_mgr = LibMgr()
        LibMgr.LIB = 'invalidmodule'
        assert lib_mgr.is_available() == False
