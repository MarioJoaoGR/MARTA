# Module: pysnooper.pycompat
import pytest
from pysnooper.pycompat import PathLike

# Test cases for the __subclasshook__ method of the PathLike class
def test_pathlike_subclasshook_fspath():
    """Test if a subclass with __fspath__ is recognized as a path-like object."""
    class MyPathClass(PathLike):
        def __fspath__(self):
            return '/my/custom/path'
    
    assert issubclass(MyPathClass, PathLike)

def test_pathlike_subclasshook_open():
    """Test if a subclass with open method and 'path' in its name is recognized as a path-like object."""
    class FilePathClass(PathLike):
        def open(self):
            pass
    
    assert issubclass(FilePathClass, PathLike)

def test_pathlike_subclasshook_no_fspath_or_open():
    """Test if a subclass without __fspath__ and without 'path' in its name or open method is not recognized as a path-like object."""
    class NonPathLikeClass:
        pass
    
    assert not issubclass(NonPathLikeClass, PathLike)

def test_pathlike_subclasshook_both_fspath_and_open():
    """Test if a subclass with both __fspath__ and open methods is recognized as a path-like object."""
    class HybridPathClass(PathLike):
        def __fspath__(self):
            return '/my/custom/path'
        
        def open(self):
            pass
    
    assert issubclass(HybridPathClass, PathLike)

if __name__ == "__main__":
    pytest.main()
