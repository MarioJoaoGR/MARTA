
import pytest
from pytutils.timers import Timer
import time

@pytest.fixture(scope="function")
def timer():
    return Timer(name='Operation', verbose=True)

def test_valid_input(timer):
    with timer:
        # Simulate some operation that takes time
        time.sleep(1)
