
import pytest
from ansible.executor.stats import AggregateStats

def test_valid_increment():
    stats = AggregateStats()
    host = 'host1'
    what = 'failures'

    # Initial state should be empty
    assert not getattr(stats, what).get(host, 0)

    # Increment the statistic with None (should raise TypeError if not handled correctly)
    with pytest.raises(TypeError):
        stats.increment(None, host)

def test_edge_case_none():
    stats = AggregateStats()
    host = 'host1'
    what = 'failures'

    # Initial state should be empty
    assert not getattr(stats, what).get(host, 0)

    # Increment the statistic with None (should raise TypeError if not handled correctly)
    with pytest.raises(TypeError):
        stats.increment(None, host)
