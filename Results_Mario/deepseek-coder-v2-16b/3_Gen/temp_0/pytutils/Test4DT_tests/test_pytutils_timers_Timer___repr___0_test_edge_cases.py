
from pytutils.timers import Timer
import pytest

@pytest.fixture
def timer():
    return Timer(name='test_timer', verbose=True)

def test_repr_with_name(timer):
    assert repr(timer) == 'Timer(test_timer)'

def test_repr_without_name(timer):
    # Create a new instance without name for testing the default behavior
    timer_no_name = Timer()
    assert repr(timer_no_name) == 'Timer()'
