
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
    # Test decrementing a statistic for a nonexistent host, which should initialize the count to zero
    aggregate_stats.decrement('processed', 'non_existent_host')
    assert aggregate_stats.processed['non_existent_host'] == 0

def test_decrement_negative_count(aggregate_stats):
    # Test decrementing a statistic where the count is already zero, which should not raise an error but stay at zero
    aggregate_stats.failures['host1'] = 0
    aggregate_stats.decrement('failures', 'host1')
    assert aggregate_stats.failures['host1'] == 0
