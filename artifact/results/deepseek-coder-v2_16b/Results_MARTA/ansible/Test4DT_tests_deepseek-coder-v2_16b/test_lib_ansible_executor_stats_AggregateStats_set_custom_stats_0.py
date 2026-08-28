
import pytest
from lib.ansible.executor.stats import AggregateStats

def test_set_custom_stats():
    stats = AggregateStats()
    
    # Test setting custom statistic for a specific host
    stats.set_custom_stats('memory_usage', 128, 'host1')
    assert 'memory_usage' in stats.custom['host1']
    assert stats.custom['host1']['memory_usage'] == 128
    
    # Test setting custom statistic for the global run
    stats.set_custom_stats('cpu_usage', 4, '_run')
    assert 'cpu_usage' in stats.custom['_run']
    assert stats.custom['_run']['cpu_usage'] == 4
    
    # Test setting custom statistic with default host if none is provided
    stats.set_custom_stats('disk_space', 256)
    assert 'disk_space' in stats.custom['_run']
    assert stats.custom['_run']['disk_space'] == 256
