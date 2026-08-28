
import pytest
from ansible.executor.stats import AggregateStats


def test_invalid_increment():
    stats = AggregateStats()
    with pytest.raises(AttributeError):
        stats.increment('invalid_key', 'host1')