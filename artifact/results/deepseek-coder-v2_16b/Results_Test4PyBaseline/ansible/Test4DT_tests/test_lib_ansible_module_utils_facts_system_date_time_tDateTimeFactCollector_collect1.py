
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