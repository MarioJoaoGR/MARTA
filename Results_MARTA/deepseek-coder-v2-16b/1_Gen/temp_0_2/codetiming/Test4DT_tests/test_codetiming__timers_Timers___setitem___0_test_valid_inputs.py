
import pytest
from codetiming import _timers as timers_module

@pytest.fixture(scope="function")
def setup():
    return timers_module.Timers()

def test_valid_inputs(setup):
    timers = setup
    assert isinstance(timers._timings, dict)
    with pytest.raises(TypeError):
        timers['test'] = 1.0
