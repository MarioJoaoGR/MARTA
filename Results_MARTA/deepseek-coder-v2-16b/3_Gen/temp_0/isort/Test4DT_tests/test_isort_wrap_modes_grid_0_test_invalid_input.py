
from typing import Any
from unittest.mock import patch

import pytest

from isort.wrap_modes import grid as isort_grid


@pytest.fixture(params=[{}])
def interface(request):
    return request.param

def test_invalid_input(interface: dict[str, Any]):
    with pytest.raises(KeyError):
        isort_grid(**interface)
