
import pytest
from unittest.mock import MagicMock

class X:
    def __len__(self):
        return 1 << 31

def test_edge_case():
    x = X()
    assert len(x) == (1 << 31)
