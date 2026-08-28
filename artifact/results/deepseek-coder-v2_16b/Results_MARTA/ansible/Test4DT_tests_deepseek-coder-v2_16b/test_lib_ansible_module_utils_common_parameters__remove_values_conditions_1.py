
import pytest
import datetime
from ansible.module_utils.common.parameters import _remove_values_conditions

def test_valid_case_string():
    value = 'sensitive_string'
    no_log_strings = {'sensitive', 'secret'}
    deferred_removals = []
    
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_valid_case_list():
    value = ['sensitive', 'data']
    no_log_strings = {'data'}
    deferred_removals = []
    
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == []

def test_error_case_none():
    value = None
    no_log_strings = set()
    deferred_removals = []
    
    with pytest.raises(TypeError):
        _remove_values_conditions(value, no_log_strings, deferred_removals)
