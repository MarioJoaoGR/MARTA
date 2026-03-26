
import os
from typing import Iterable

def _abspaths(cwd: str, values: Iterable[str]) -> set[str]:
    paths = {
        (
            os.path.join(cwd, value)
            if not value.startswith(os.path.sep) and value.endswith(os.path.sep)
            else value
        )
        for value in values
    }
    return paths

import pytest

def test_edge_case_none():
    with pytest.raises(TypeError):
        _abspaths("cwd", None)
