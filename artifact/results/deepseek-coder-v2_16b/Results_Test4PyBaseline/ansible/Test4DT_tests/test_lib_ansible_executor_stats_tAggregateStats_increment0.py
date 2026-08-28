# Module: ansible.executor.stats
import pytest
from lib.ansible.executor.stats import AggregateStats

# Test initialization of the AggregateStats class
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

# Test incrementing the processed statistic for a host
def test_increment_processed():
    aggregate_stats = AggregateStats()
    aggregate_stats.increment('processed', 'host1')
    assert aggregate_stats.processed['host1'] == 1

# Test incrementing the failures statistic for a host
def test_increment_failures():
    aggregate_stats = AggregateStats()
    aggregate_stats.increment('failures', 'host2')
    assert aggregate_stats.failures['host2'] == 1

# Test incrementing the ok statistic for a host
def test_increment_ok():
    aggregate_stats = AggregateStats()
    aggregate_stats.increment('ok', 'host3')
    assert aggregate_stats.ok['host3'] == 1

# Test adding custom stats for a specific host
def test_set_custom_stats():
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('errors', 2, 'host1')
    assert aggregate_stats.custom['host1']['errors'] == 2

# Test updating custom stats for a specific host
def test_update_custom_stats():
    aggregate_stats = AggregateStats()
    aggregate_stats.set_custom_stats('warnings', 1, 'host1')
    aggregate_stats.update_custom_stats('warnings', 3, 'host1')
    assert aggregate_stats.custom['host1']['warnings'] == 4

# Test summarizing statistics for a specific host
def test_summarize():
    aggregate_stats = AggregateStats()
    aggregate_stats.increment('processed', 'host1')
    aggregate_stats.increment('failures', 'host2')
    aggregate_stats.increment('ok', 'host3')
    
    host_info = aggregate_stats.summarize('localhost')
    assert isinstance(host_info, dict)
    assert set(host_info.keys()) == {'processed', 'failures', 'ok'}
    assert host_info['processed'] == 0
    assert host_info['failures'] == 0
    assert host_info['ok'] == 0
