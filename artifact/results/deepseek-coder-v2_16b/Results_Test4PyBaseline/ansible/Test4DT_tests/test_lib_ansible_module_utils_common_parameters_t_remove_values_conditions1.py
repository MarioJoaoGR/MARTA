
import pytest
import datetime
from ansible.module_utils.common.parameters import _remove_values_conditions

def test_handling_unknown_type():
    value = object()  # An unknown type
    no_log_strings = set()
    deferred_removals = []
    with pytest.raises(TypeError):
        _remove_values_conditions(value, no_log_strings, deferred_removals)

def test_handling_datetime_object():
    value = datetime.datetime.now()
    no_log_strings = set()
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert isinstance(sanitized_value, str), "Expected datetime object to be converted to string"

def test_handling_sensitive_string():
    value = "sensitive info"
    no_log_strings = {"info"}
    deferred_removals = []
    sanitized_value = _remove_values_conditions(value, no_log_strings, deferred_removals)