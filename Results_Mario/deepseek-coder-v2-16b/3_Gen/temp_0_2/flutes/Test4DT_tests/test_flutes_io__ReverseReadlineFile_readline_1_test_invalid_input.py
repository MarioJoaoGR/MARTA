
import pytest
from flutes.io import _ReverseReadlineFile

def test_invalid_input():
    # Test with non-iterable object as gen parameter
    fp = None  # Assuming `None` is an invalid file pointer for the purpose of this test
    gen = None  # Assuming `None` is a non-iterable generator for the purpose of this test
    reverse_readline = _ReverseReadlineFile(fp, gen)
    
    with pytest.raises(TypeError):
        next(reverse_readline)
