
import pytest
from unittest.mock import MagicMock

class X:
    def __len__(self):
        return 1 << 31

def test_valid_input():
    x = X()
    assert len(x) == (1 << 31), "Expected length is 2^31"
