
import pytest
import random
from pytutils.rand import rand_hex

@pytest.mark.parametrize("invalid_input", [None, "string", [], {}])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        rand_hex(length=invalid_input)
