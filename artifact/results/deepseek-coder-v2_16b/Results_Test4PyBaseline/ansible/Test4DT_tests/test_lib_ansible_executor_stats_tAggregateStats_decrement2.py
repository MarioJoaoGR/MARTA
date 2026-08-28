
# Module: ansible.executor.stats
# test_aggregate_stats.py
from ansible.executor.stats import AggregateStats
import pytest

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_decrement_existing_host(aggregate_stats):
    # Test decrementing a statistic for an existing host
    aggregate_stats.processed['host1'] = 2
    aggregate_stats.decrement('processed', 'host1')
    assert aggregate_stats.processed['host1'] == 1

def test_decrement_nonexistent_host(aggregate_stats):
    # Test decrementing a statistic for a nonexistent host, should initialize to zero
    aggregate_stats.decrement('processed', 'host2')