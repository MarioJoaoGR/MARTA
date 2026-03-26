
import os
import pytest
from unittest.mock import patch

def expand(val: str) -> str:
    val = os.path.expandvars(val)
    val = os.path.expanduser(val)
    return val

@pytest.mark.parametrize("invalid_input", [123, None, [], {}])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        expand(invalid_input)
