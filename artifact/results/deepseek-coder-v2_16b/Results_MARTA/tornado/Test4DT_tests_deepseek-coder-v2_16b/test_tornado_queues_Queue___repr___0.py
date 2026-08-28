
import pytest
from tornado.queues import Queue



def test_invalid_input_negative():
    """Test that creating a Queue with maxsize -1 raises ValueError."""
    with pytest.raises(ValueError) as e:
        q = Queue(maxsize=-1)
    assert str(e.value) == "maxsize can't be negative"

def test_valid_input():
    """Test that creating a Queue with valid maxsize works."""
    q = Queue(maxsize=2)
    assert isinstance(q, Queue)
    assert q._maxsize == 2

def test_default_maxsize():
    """Test that creating a Queue without specifying maxsize uses the default value (0)."""
    q = Queue()
    assert q._maxsize == 0