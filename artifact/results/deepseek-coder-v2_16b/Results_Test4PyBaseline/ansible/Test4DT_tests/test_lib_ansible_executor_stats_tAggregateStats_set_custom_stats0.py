
import pytest
from ansible.executor.stats import AggregateStats

# Test initialization of AggregateStats instance
def test_aggregate_stats_initialization():
    aggregate_stats = AggregateStats()
    assert isinstance(aggregate_stats, AggregateStats)
    assert aggregate_stats.processed == {}
    assert aggregate_stats.failures == {}
    assert aggregate_stats.ok == {}
    assert aggregate_stats.dark == {}
    assert aggregate_stats.changed == {}
    assert aggregate_stats.skipped == {}
    assert aggregate_stats.rescued == {}
    assert aggregate_stats.ignored == {}
    assert aggregate_stats.custom == {}

# Test setting custom stats without a host
def test_set_custom_stats_without_host():
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('errors', 2)
    assert aggregate_stats.custom['_run'] == {'errors': 2}

# Test setting custom stats with a specific host
def test_set_custom_stats_with_host():
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('errors', 2, 'host1')
    assert aggregate_stats.custom == {'host1': {'errors': 2}}

# Test updating custom stats for an existing host
def test_update_custom_stats():
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('errors', 2, 'host1')
    aggregate_stats.set_custom_stats('warnings', 1, 'host1')
    assert aggregate_stats.custom == {'host1': {'errors': 2, 'warnings': 1}}

# Test setting custom stats for a new host
def test_set_custom_stats_new_host():
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('errors', 2, 'host2')