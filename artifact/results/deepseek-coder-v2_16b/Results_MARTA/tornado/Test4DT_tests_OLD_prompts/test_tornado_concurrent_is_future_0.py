
import pytest
from typing import Any
from unittest.mock import patch

class FUTURES:
    pass

def is_future(x: Any) -> bool:
    return isinstance(x, FUTURES)

@pytest.mark.parametrize("input_obj", [FUTURES(), "not a future"])
def test_is_future(input_obj):
    assert is_future(input_obj) == (type(input_obj) == FUTURES)
