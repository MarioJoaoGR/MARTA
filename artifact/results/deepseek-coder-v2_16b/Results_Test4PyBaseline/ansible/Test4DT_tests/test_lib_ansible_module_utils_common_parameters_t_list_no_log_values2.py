
import pytest
from ansible.module_utils.common.parameters import _list_no_log_values

# Test case to cover line 308: no_log_values = set()
def test_initialization():
    argument_spec = {'param1': {'no_log': True}}
    params = {'param1': "sensitive data"}
    result = _list_no_log_values(argument_spec, params)
    assert isinstance(result, set), f"Expected a set but got {type(result)}"