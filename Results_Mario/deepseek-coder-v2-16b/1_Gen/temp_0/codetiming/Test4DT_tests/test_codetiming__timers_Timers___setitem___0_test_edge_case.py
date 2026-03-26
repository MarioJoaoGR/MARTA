
import pytest
from codetiming._timers import Timers

def test_edge_case():
    timers = Timers()
    with pytest.raises(TypeError):
        timers['test'] = None
