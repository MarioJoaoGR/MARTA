
# Module: ansible.executor.stats
# test_aggregate_stats.py
from ansible.executor.stats import AggregateStats
import pytest

@pytest.fixture
def aggregate_stats():
    return AggregateStats()

def test_initialization(aggregate_stats):
    assert isinstance(aggregate_stats, AggregateStats)
    assert all(isinstance(getattr(aggregate_stats, attr), dict) for attr in [
        'processed', 'failures', 'ok', 'dark', 'changed', 'skipped', 'rescued', 'ignored', 'custom'
    ])

def test_increment_and_summarize(aggregate_stats):
    aggregate_stats.increment('processed', 'host1')
    aggregate_stats.increment('failures', 'host2')
    aggregate_stats.increment('ok', 'host3')
    
    host_info = aggregate_stats.summarize('host1')
    assert host_info['ok'] == 0
    assert host_info['failures'] == 0
    assert host_info['unreachable'] == 0
    assert host_info['changed'] == 0
    assert host_info['skipped'] == 0
    assert host_info['rescued'] == 0
    assert host_info['ignored'] == 0
    
    host_info = aggregate_stats.summarize('host2')
    assert host_info['ok'] == 0
    assert host_info['failures'] == 1
    assert host_info['unreachable'] == 0
    assert host_info['changed'] == 0
    assert host_info['skipped'] == 0
    assert host_info['rescued'] == 0
    assert host_info['ignored'] == 0
    
    host_info = aggregate_stats.summarize('host3')
    assert host_info['ok'] == 1
    assert host_info['failures'] == 0
    assert host_info['unreachable'] == 0
    assert host_info['changed'] == 0
    assert host_info['skipped'] == 0
    assert host_info['rescued'] == 0
    assert host_info['ignored'] == 0

def test_set_and_update_custom_stats(aggregate_stats):
    aggregate_stats.set_custom_stats('specific_metric', 5, 'host4')
    assert aggregate_stats.custom['host4']['specific_metric'] == 5
    
    aggregate_stats.update_custom_stats('specific_metric', {'additional_metric': 3}, 'host4')
    assert aggregate_stats.custom['host4']['specific_metric'] == 8

def test_summarize_method(aggregate_stats):
    # Assuming some data has been added to stats...
    host_info = aggregate_stats.summarize('localhost')
    assert isinstance(host_info, dict)
    assert all(isinstance(value, int) for value in host_info.values())
