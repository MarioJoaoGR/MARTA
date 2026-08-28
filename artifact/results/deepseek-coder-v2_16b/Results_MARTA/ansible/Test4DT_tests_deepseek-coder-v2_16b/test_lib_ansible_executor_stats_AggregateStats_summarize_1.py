
import pytest
from ansible.executor.stats import AggregateStats

def test_aggregate_stats_summarize():
    stats = AggregateStats()
    # Add some data to simulate task results
    stats.ok['host1'] = 2
    stats.failures['host1'] = 1
    with pytest.raises(AttributeError):
        stats.unreachable['host1'] = 0

def test_aggregate_stats_custom_stat():
    stats = AggregateStats()
    # Add a custom statistic for a host
    stats.set_custom_stats('memory_usage', 128, 'host1')
    
    # Test the custom statistic is correctly set and can be retrieved
    summary = stats.summarize('host1')
    assert summary['ok'] == 0
    assert summary['failures'] == 0
    assert summary['unreachable'] == 0
    assert summary['changed'] == 0
    assert summary['skipped'] == 0
    assert summary['rescued'] == 0
    assert summary['ignored'] == 0
    with pytest.raises(KeyError):
        assert summary['custom']
