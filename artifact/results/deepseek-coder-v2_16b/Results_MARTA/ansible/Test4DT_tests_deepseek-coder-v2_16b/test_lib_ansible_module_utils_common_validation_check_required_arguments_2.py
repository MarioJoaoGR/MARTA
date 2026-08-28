
import pytest
from ansible.module_utils.common.validation import check_required_arguments

def test_valid_case():
    argument_spec = {'param1': {'required': True}, 'param2': {'required': False}}
    parameters = {'param1': 1}
    missing_params = check_required_arguments(argument_spec, parameters)
    assert missing_params == ['param2']

def test_edge_case():
    argument_spec = {'param1': {'required': True}, 'param2': {'required': False}}
    parameters = None
    with pytest.raises(TypeError) as excinfo:
        check_required_arguments(argument_spec, parameters)
    assert str(excinfo.value) == "missing required arguments: param1"

def test_error_case():
    argument_spec = {'param1': {'required': True}, 'param2': {'required': False}}
    parameters = {}
    with pytest.raises(TypeError) as excinfo:
        check_required_arguments(argument_spec, parameters)
    assert str(excinfo.value) == "missing required arguments: param1"
