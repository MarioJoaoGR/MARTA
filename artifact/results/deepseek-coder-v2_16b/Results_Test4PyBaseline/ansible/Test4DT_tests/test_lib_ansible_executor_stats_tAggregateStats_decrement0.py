# Module: ansible.executor.stats
# test_aggregate_stats.py
from ansible.executor.stats import AggregateStats
import pytest

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_increment(aggregate_stats):
    # Test incrementing a statistic for a host
    aggregate_stats.increment('processed', 'host1')
    assert aggregate_stats.processed['host1'] == 1

def test_decrement(aggregate_stats):
    # Test decrementing a statistic for a host
    aggregate_stats.failures['host2'] = 1
    aggregate_stats.decrement('failures', 'host2')
    assert aggregate_stats.failures['host2'] == 0

def test_set_custom_stats(aggregate_stats):
    # Test setting custom stats for a host
    aggregate_stats.set_custom_stats('errors', 2, 'host1')
    assert aggregate_stats.custom['host1']['errors'] == 2

def test_decrement_raises_keyerror(aggregate_stats):
    # Test decrementing a statistic that should raise KeyError if below zero
    with pytest.raises(KeyError):
        aggregate_stats.failures['host3'] = -1
        aggregate_stats.decrement('failures', 'host3')

def test_summarize(aggregate_stats):
    # Test summarizing statistics for a host
    aggregate_stats.processed['localhost'] = 5
    aggregate_stats.failures['localhost'] = 2
    aggregate_stats.ok['localhost'] = 3
    host_info = aggregate_stats.summarize('localhost')
    assert host_info == {
        'processed': 5,
        'failures': 2,
        'ok': 3
    }
