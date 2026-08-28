
import pytest
from ansible.executor.stats import AggregateStats

# Test setting custom stats without a host (line 76)
def test_set_custom_stats_without_host():
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('errors', 2)
    assert aggregate_stats.custom['_run'] == {'errors': 2}

# Test setting custom stats with a specific host (line 78)
def test_set_custom_stats_with_host():
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('errors', 2, 'host1')
    assert aggregate_stats.custom == {'host1': {'errors': 2}}

# Test updating custom stats for an existing host (line 81)
def test_update_custom_stats():
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('errors', 2, 'host1')
    aggregate_stats.set_custom_stats('warnings', 1, 'host1')
    assert aggregate_stats.custom == {'host1': {'errors': 2, 'warnings': 1}}

# Test setting custom stats for a new host (line 79)
def test_set_custom_stats_new_host():
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('errors', 2, 'host2')
    assert aggregate_stats.custom == {'host2': {'errors': 2}}
