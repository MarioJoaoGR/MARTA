
import pytest
from tornado.locks import Semaphore

def test_error_case():
    # Test that creating a Semaphore with an initial value less than 0 raises a ValueError
    with pytest.raises(ValueError):
        Semaphore(-1)
