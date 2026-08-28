# Module: ansible.module_utils.common.parameters
import pytest
import datetime
from typing import Union, List, Tuple, Set, Dict, Any

# Import the function from its module
from ansible.module_utils.common.parameters import _remove_values_conditions

def test_sanitizing_string_with_sensitive_info():
    value = "sensitive info"
    no_log_strings = {"info"}
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert sanitized_value == '********'

def test_sanitizing_datetime_object():
    value = datetime.datetime.now()
    no_log_strings = set()
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert isinstance(sanitized_value, str)  # It should be the ISO format of the current datetime

def test_sanitizing_complex_dict_with_sensitive_info():
    value = {'a': "sensitive info", 'b': [{"c": "info"}]}
    no_log_strings = {"info"}
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert sanitized_value == {}  # All sensitive information is replaced or removed

def test_sanitizing_list_of_strings():
    value = ["sensitive info", "another sensitive string"]
    no_log_strings = {"info"}
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert sanitized_value == ['********', '********']

def test_sanitizing_set_of_numbers():
    value = {12345, 67890}
    no_log_strings = {"info"}
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert sanitized_value == {12345, 67890}  # No change since it's a set of numbers

def test_sanitizing_scalar_types():
    value = "sensitive info"
    no_log_strings = {"info"}
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert sanitized_value == '********'

def test_sanitizing_datetime_object():
    value = datetime.datetime.now()
    no_log_strings = set()
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert isinstance(sanitized_value, str)  # It should be the ISO format of the current datetime

def test_sanitizing_complex_dict_with_sensitive_info():
    value = {'a': "sensitive info", 'b': [{"c": "info"}]}
    no_log_strings = {"info"}
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert sanitized_value == {}  # All sensitive information is replaced or removed

def test_sanitizing_list_of_strings():
    value = ["sensitive info", "another sensitive string"]
    no_log_strings = {"info"}
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert sanitized_value == ['********', '********']

def test_sanitizing_set_of_numbers():
    value = {12345, 67890}
    no_log_strings = {"info"}
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert sanitized_value == {12345, 67890}  # No change since it's a set of numbers
