
import pytest
from enum import Enum
from typing import Any

class PathAction(Enum):
    KEY = 1
    INDEX = 2
    APPEND = 3

def object_for(kind: PathAction) -> Any:
    if kind is PathAction.KEY:
        return {}
    elif kind in {PathAction.INDEX, PathAction.APPEND}:
        return []
    else:
        assert False, "This should not happen"

def test_invalid_inputs():
    with pytest.raises(AssertionError):
        object_for(PathAction.KEY)  # This should pass as expected
        object_for("INVALID")       # This should raise an AssertionError
