
import os
import pytest
from unittest.mock import patch

def expand(val: str) -> str:
    val = os.path.expandvars(val)
    val = os.path.expanduser(val)
    return val

@pytest.mark.parametrize("input_value", [None])
def test_edge_case_none(input_value):
    with pytest.raises(TypeError):
        expand(input_value)
