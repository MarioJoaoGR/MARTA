
import pytest
from httpie.utils import humanize_bytes

def test_error_case_invalidPrecision():
    with pytest.raises(TypeError):
        humanize_bytes("invalid input", precision="not an integer")
