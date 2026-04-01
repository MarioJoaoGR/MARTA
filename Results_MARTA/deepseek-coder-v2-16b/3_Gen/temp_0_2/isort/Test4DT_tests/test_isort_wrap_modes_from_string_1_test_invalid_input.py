
import pytest
from isort.wrap_modes import WrapModes, from_string

@pytest.mark.parametrize("invalid_input", ["invalid_wrap_mode", 999])
def test_invalid_input(invalid_input):
    with pytest.raises(ValueError):
        from_string(invalid_input)
