
import pytest
from flutes.fs import readable_size

def test_error_case_2():
    with pytest.raises(TypeError):
        assert readable_size("invalid input")
