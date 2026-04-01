
import pytest
from flutes.iterator import split_by

def test_error_case_none():
    iterable = None
    separator = ' '
    
    with pytest.raises(TypeError):
        list(split_by(iterable, empty_segments=False, separator=separator))
