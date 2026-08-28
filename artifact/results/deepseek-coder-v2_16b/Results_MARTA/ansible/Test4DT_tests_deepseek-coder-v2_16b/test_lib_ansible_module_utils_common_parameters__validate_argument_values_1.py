
import pytest
from ansible.module_utils.common.parameters import ArgumentValueError, ArgumentTypeError, AnsibleValidationErrorMultiple

def _validate_argument_values(argument_spec, parameters, options_context=None, errors=None):
    if errors is None:
        errors = AnsibleValidationErrorMultiple()

    for param, spec in argument_spec.items():
        choices = spec.get('choices')
        if choices is None:
            continue

        if isinstance(choices, (frozenset, KeysView, Sequence)) and not isinstance(choices, (binary_type, text_type)):
            if param in parameters:
                if isinstance(parameters[param], list):
                    diff_list = ", ".join([item for item in parameters[param] if item not in choices])
                    if diff_list:
                        choices_str = ", ".join([to_native(c) for c in choices])
                        msg = "value of %s must be one or more of: %s. Got no match for: %s" % (param, choices_str, diff_list)
                        if options_context:
                            msg = "{0} found in {1}".format(msg, " -> ".join(options_context))
                        errors.append(ArgumentValueError(msg))
                elif parameters[param] not in choices:
                    choices_str = ", ".join([to_native(c) for c in choices])
                    msg = "value of %s must be one of: %s, got: %s" % (param, choices_str, parameters[param])
                    if options_context:
                        msg = "{0} found in {1}".format(msg, " -> ".join(options_context))
                    errors.append(ArgumentValueError(msg))
        else:
            msg = "internal error: choices for argument %s are not iterable: %s" % (param, choices)
            if options_context:
                msg = "{0} found in {1}".format(msg, " -> ".join(options_context))
            errors.append(ArgumentTypeError(msg))

# Test scenarios
def test_valid_inputs():
    argument_spec = {'param1': {'type': 'str', 'choices': ['val1', 'val2']}, 'param2': {'type': 'int'}}
    parameters = {'param1': 'val1', 'param2': 5}
    options_context = None
    errors = AnsibleValidationErrorMultiple()
    
    _validate_argument_values(argument_spec, parameters, options_context=options_context, errors=errors)
    assert not errors.messages, "Errors occurred: {}".format(errors.messages)

def test_edge_cases():
    argument_spec = {'param1': {'type': 'str', 'choices': ['val1', 'val2']}, 'param2': {'type': 'int'}}
    parameters = {'param1': 'invalid_value', 'param2': 5}
    options_context = None
    errors = AnsibleValidationErrorMultiple()
    
    with pytest.raises(AssertionError):
        _validate_argument_values(argument_spec, parameters, options_context=options_context, errors=errors)
    assert "value of param1 must be one of: val1, val2" in str(errors.messages), "Expected error not found."

def test_invalid_inputs():
    argument_spec = {'param1': {'type': 'str', 'choices': ['val1', 'val2']}, 'param2': {'type': 'int'}}
    parameters = {'param1': 'val3', 'param2': 5}
    options_context = None
    errors = AnsibleValidationErrorMultiple()
    
    with pytest.raises(AssertionError):
        _validate_argument_values(argument_spec, parameters, options_context=options_context, errors=errors)
    assert "value of param1 must be one of: val1, val2" in str(errors.messages), "Expected error not found."
