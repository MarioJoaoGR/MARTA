
from typing import Any, List

import pytest

from isort.literal import _unique_list


class MockPrinter:
    def pformat(self, value: List[Any]) -> str:
        return ','.join(map(str, sorted(set(value))))

def test_invalid_input():
    with pytest.raises(TypeError):
        _unique_list(None, MockPrinter())
