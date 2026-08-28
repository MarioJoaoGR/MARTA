
import pytest
from ansible.module_utils.common.validation import check_required_arguments


def test_missing_required_parameter():
    argument_spec = {'param1': {'required': True}, 'param2': {'required': False}}
    parameters = {}
    with pytest.raises(TypeError) as excinfo:
        check_required_arguments(argument_spec, parameters)
    assert str(excinfo.value) == "missing required arguments: param1"
