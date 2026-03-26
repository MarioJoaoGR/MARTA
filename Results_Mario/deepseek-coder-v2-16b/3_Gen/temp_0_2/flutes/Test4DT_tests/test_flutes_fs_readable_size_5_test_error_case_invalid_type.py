
import pytest
from flutes.fs import readable_size

def test_error_case_invalid_type():
    with pytest.raises(TypeError):
        readable_size("invalid_type")
