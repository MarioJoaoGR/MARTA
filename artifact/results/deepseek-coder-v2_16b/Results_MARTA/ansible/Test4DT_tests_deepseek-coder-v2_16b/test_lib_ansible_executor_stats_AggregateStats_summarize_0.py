
import pytest
from ansible.executor.stats import AggregateStats

def test_invalid_input():
    stats = AggregateStats()
    with pytest.raises(TypeError):
        # This should raise a TypeError because __init__ does not accept any parameters
        AggregateStats("invalid_parameter")
