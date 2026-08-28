
import pytest
from ansible.executor.stats import AggregateStats



def test_update_custom_stats_with_valid_type():
    stats = AggregateStats()
    stats.update_custom_stats('memory_usage', 128, 'host1')
    assert stats.custom['host1']['memory_usage'] == 128

def test_update_custom_stats_with_valid_type_global():
    stats = AggregateStats()
    stats.update_custom_stats('memory_usage', 128, '_run')
    assert stats.custom['_run']['memory_usage'] == 128