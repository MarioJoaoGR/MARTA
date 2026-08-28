# Module: ansible.module_utils.facts.system.date_time
import pytest
from ansible.module_utils.facts.system.date_time import DateTimeFactCollector
import datetime
import time

# Create an instance of DateTimeFactCollector
@pytest.fixture(scope="module")
def date_time_collector():
    return DateTimeFactCollector()

# Test the collect method with default parameters
def test_collect_default(date_time_collector):
    collected_facts = date_time_collector.collect()
    assert 'date_time' in collected_facts
    date_time_facts = collected_facts['date_time']
    
    # Check if the current time is being used to populate facts
    now = datetime.datetime.now()
    assert date_time_facts['year'] == str(now.year)
    assert date_time_facts['month'] == now.strftime('%m')
    assert date_time_facts['weekday'] == now.strftime('%A')
    assert date_time_facts['weekday_number'] == now.strftime('%w')
    assert date_time_facts['weeknumber'] == now.strftime('%W')
    assert date_time_facts['day'] == now.strftime('%d')
    assert date_time_facts['hour'] == now.strftime('%H')
    assert date_time_facts['minute'] == now.strftime('%M')
    assert date_time_facts['second'] == now.strftime('%S')
    assert date_time_facts['epoch'] == str(int(time.time()))
    assert date_time_facts['epoch_int'] == str(int(now.strftime('%s')))
    assert date_time_facts['date'] == now.strftime('%Y-%m-%d')
    assert date_time_facts['time'] == now.strftime('%H:%M:%S')
    iso8601_micro = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert date_time_facts['iso8601_micro'] == iso8601_micro
    iso8601 = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert date_time_facts['iso8601'] == iso8601
    iso8601_basic = now.strftime("%Y%m%dT%H%M%S%f")
    assert date_time_facts['iso8601_basic'] == iso8601_basic
    iso8601_basic_short = now.strftime("%Y%m%dT%H%M%S")
    assert date_time_facts['iso8601_basic_short'] == iso8601_basic_short
    assert date_time_facts['tz'] == time.strftime("%Z")
    assert date_time_facts['tz_dst'] == time.tzname[1]
    assert date_time_facts['tz_offset'] == time.strftime("%z")

# Test the collect method with provided module and collected_facts parameters (should not affect the function)
def test_collect_with_params(date_time_collector):
    collected_facts = date_time_collector.collect(module=None, collected_facts={})
    assert 'date_time' in collected_facts
    date_time_facts = collected_facts['date_time']
    
    # Check if the current time is being used to populate facts (same as default test)
    now = datetime.datetime.now()
    assert date_time_facts['year'] == str(now.year)
    assert date_time_facts['month'] == now.strftime('%m')
    assert date_time_facts['weekday'] == now.strftime('%A')
    assert date_time_facts['weekday_number'] == now.strftime('%w')
    assert date_time_facts['weeknumber'] == now.strftime('%W')
    assert date_time_facts['day'] == now.strftime('%d')
    assert date_time_facts['hour'] == now.strftime('%H')
    assert date_time_facts['minute'] == now.strftime('%M')
    assert date_time_facts['second'] == now.strftime('%S')
    assert date_time_facts['epoch'] == str(int(time.time()))
    assert date_time_facts['epoch_int'] == str(int(now.strftime('%s')))
    assert date_time_facts['date'] == now.strftime('%Y-%m-%d')
    assert date_time_facts['time'] == now.strftime('%H:%M:%S')
    iso8601_micro = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    assert date_time_facts['iso8601_micro'] == iso8601_micro
    iso8601 = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert date_time_facts['iso8601'] == iso8601
    iso8601_basic = now.strftime("%Y%m%dT%H%M%S%f")
    assert date_time_facts['iso8601_basic'] == iso8601_basic
    iso8601_basic_short = now.strftime("%Y%m%dT%H%M%S")
    assert date_time_facts['iso8601_basic_short'] == iso8601_basic_short
    assert date_time_facts['tz'] == time.strftime("%Z")
    assert date_time_facts['tz_dst'] == time.tzname[1]
    assert date_time_facts['tz_offset'] == time.strftime("%z")
