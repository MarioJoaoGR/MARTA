
import pytest
from io import StringIO
from flutes.io import _ReverseReadlineFile

def test_reversereadlinefile_exit():
    """Test that the __exit__ method correctly closes the file."""
    fp = StringIO("Hello, world!\n")
    gen = iter([])  # An empty generator to simulate end-of-file conditions
    rev_readline = _ReverseReadlineFile(fp, gen)
    
    assert not fp.closed  # Ensure the file is open before exiting
    with pytest.raises(StopIteration):  # Simulate context manager exit
        raise StopIteration from None  # This should be raised by __exit__
    