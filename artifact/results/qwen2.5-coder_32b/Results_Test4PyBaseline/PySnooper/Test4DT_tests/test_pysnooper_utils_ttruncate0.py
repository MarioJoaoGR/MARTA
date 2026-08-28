
import pytest
from pysnooper.utils import truncate

def test_truncate_within_max_length():
    assert truncate("Short", 10) == "Short"
    assert truncate("Another example", 20) == "Another example"

def test_truncate_exceeds_max_length():
    assert truncate("Hello, world!", 10) == "Hel...rld!"