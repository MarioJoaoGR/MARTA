
import pytest
from ansible.executor.stats import AggregateStats

def test_set_custom_stats():
    stats = AggregateStats()
    with pytest.raises(TypeError):
        # Attempting to set custom statistics without parameters should raise a TypeError
        stats.set_custom_stats('memory_usage')
