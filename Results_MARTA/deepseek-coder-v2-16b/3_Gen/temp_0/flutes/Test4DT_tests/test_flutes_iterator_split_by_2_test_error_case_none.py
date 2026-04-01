
import pytest
from flutes.iterator import split_by

def test_error_case_none():
    with pytest.raises(TypeError):
        list(split_by(None, empty_segments=False, separator=' '))
