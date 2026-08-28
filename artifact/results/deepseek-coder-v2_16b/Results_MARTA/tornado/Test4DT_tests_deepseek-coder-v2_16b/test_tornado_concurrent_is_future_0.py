
import pytest
from typing import Any

# Assuming FUTURES is defined in a module or imported correctly
class FUTURES: pass

def is_future(x: Any) -> bool:
    return isinstance(x, FUTURES)

# Test cases
def test_valid_case():
    futures = FUTURES()
    assert is_future(futures) == True

def test_invalid_case():
    x = 'not a future'
    assert is_future(x) == False

def test_edge_case():
    x = None
    assert is_future(x) == False
