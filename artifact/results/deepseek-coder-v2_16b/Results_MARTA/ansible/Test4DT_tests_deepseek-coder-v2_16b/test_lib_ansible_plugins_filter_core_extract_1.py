
import pytest
from ansible.plugins.filter.core import extract as core_extract

# Test case 1: Basic usage of extract function
def test_basic_usage():
    data = {'a': {'b': {'c': 1}}}
    environment = type('Environment', (object,), {'getitem': lambda self, container, key: container[key]})()
    result = core_extract(environment, 'a', container=data)
    assert result == {'b': {'c': 1}}

# Test case 2: Usage with more keys
def test_usage_with_more_keys():
    data = {'a': {'b': {'c': 1}}}
    environment = type('Environment', (object,), {'getitem': lambda self, container, key: container[key]})()
    result = core_extract(environment, 'a', container=data, morekeys=['b'])
    assert result == {'c': 1}

# Test case 3: Usage with None for more keys
def test_usage_with_none_for_more_keys():
    data = {'a': {'b': {'c': 1}}}
    environment = type('Environment', (object,), {'getitem': lambda self, container, key: container[key]})()
    result = core_extract(environment, 'a', container=data)
    assert result == {'b': {'c': 1}}

# Test case 4: Usage with list for more keys
def test_usage_with_list_for_more_keys():
    data = {'a': {'b': {'c': 1}}}
    environment = type('Environment', (object,), {'getitem': lambda self, container, key: container[key]})()
    result = core_extract(environment, 'a', container=data, morekeys=['b'])
    assert result == {'c': 1}
