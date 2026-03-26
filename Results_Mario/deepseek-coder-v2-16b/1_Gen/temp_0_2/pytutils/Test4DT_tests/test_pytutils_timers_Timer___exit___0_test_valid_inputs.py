
import pytest
from pytutils.timers import Timer
import time

@pytest.fixture(scope="module")
def timer():
    return Timer(name='test', verbose=True)

def test_valid_inputs(timer):
    with timer:
        # Simulate a task that takes some time to complete
        time.sleep(1)
