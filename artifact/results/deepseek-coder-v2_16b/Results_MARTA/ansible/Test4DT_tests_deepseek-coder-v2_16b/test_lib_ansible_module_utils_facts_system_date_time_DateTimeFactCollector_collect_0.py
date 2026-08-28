
import pytest
from ansible.module_utils.facts.system.date_time import DateTimeFactCollector

def test_collect():
    collector = DateTimeFactCollector()
    collected_facts = {}
    result = collector.collect(collected_facts=collected_facts)
    
    assert isinstance(result, dict), "Expected a dictionary but got something else."
    assert 'date_time' in result, "Expected the key 'date_time' to be present in the result dictionary."
    
    date_time_facts = result['date_time']
    assert isinstance(date_time_facts, dict), "The value under 'date_time' should be a dictionary but it is not."
    
    expected_keys = {
        'year', 'month', 'weekday', 'weekday_number', 'weeknumber', 
        'day', 'hour', 'minute', 'second', 'epoch', 'epoch_int', 
        'date', 'time', 'iso8601_micro', 'iso8601', 'iso8601_basic', 
        'iso8601_basic_short', 'tz', 'tz_dst', 'tz_offset'
    }
    
    assert set(date_time_facts.keys()) == expected_keys, f"Expected keys {expected_keys} but got {set(date_time_facts.keys())}."
