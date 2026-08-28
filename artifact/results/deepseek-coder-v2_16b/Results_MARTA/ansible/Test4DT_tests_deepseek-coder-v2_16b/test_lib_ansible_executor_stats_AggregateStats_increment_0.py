
import pytest
from ansible.executor.stats import AggregateStats

def test_edge_increment():
    stats = AggregateStats()
    with pytest.raises(TypeError):
        stats.increment(None, 'host1')
