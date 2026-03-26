
import pytest
from flutes.io import _ReverseReadlineFile
from io import StringIO

def test_error_case():
    # Test with invalid file-like object
    fp = StringIO("Hello, world!\n")
    gen = lambda: ("!dlrow ,olleH",)  # A generator function that yields a reversed line
    rev_readline = _ReverseReadlineFile(fp, gen)
    
    with pytest.raises(TypeError):
        next(rev_readline.__iter__())
