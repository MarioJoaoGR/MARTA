
import pytest
from ansible.module_utils.common.parameters import _validate_sub_spec
from ansible.errors import AnsibleValidationErrorMultiple, SubParameterTypeError, AliasError, NoLogError, MutuallyExclusiveError, RequiredError

@pytest.mark.parametrize(
    "argument_spec, parameters, expected_errors",
    [
        (
            {
                'param1': {'type': 'str', 'options': {'secret': {'type': 'str', 'no_log': True}}},
                'param2': {'type': 'list', 'elements': 'dict', 'options': {'username': {'type': 'str'}, 'password': {'type': 'str', 'no_log': True}}}
            },
            {
                'param1': {'secret': 'supersecret'},
                'param2': [{'username': 'admin', 'password': 'mypassword'}, {'username': 'user', 'password': 'yourpassword'}]
            },
            []
        ),
        (
            {
                'param1': {'type': 'str', 'options': {'secret': {'type': 'str', 'no_log': True}}},
                'param2': {'type': 'list', 'elements': 'dict', 'options': {'username': {'type': 'str'}, 'password': {'type': 'str', 'no_log': True}}}
            },
            {
                'param1': {'secret': 'supersecret'},
                'param2': [{'username': 'admin', 'password': 'mypassword'}, {'username': 'user', 'password': 'yourpassword', 'extra': 'unsupported'}}]
            },
            [SubParameterTypeError("value of 'param2[1]' must be of type dict or list of dicts")]
        ),
        (
            {
                'param1': {'type': 'str', 'options': {'secret': {'type': 'str', 'no_log': True}}},
                'param2': {'type': 'list', 'elements': 'dict', 'options': {'username': {'type': 'str'}, 'password': {'type': 'str', 'no_log': True}}}
            },
            {
                'param1': {'secret': 'supersecret'},
                'param2': [{'username': 'admin', 'password': 'mypassword'}, {'username': 'user'}}]
            },
            [SubParameterTypeError("value of 'param2[1]' must be of type dict or list of dicts")]
        )
    ]
)
def test_validate_sub_spec(argument_spec, parameters, expected_errors):
    errors = AnsibleValidationErrorMultiple()
    _validate_sub_spec(argument_spec, parameters, prefix='options.', errors=errors)
    
    assert len(expected_errors) == len(errors.messages), "Expected errors: {}, Actual errors: {}".format(expected_errors, errors.messages)
    for i, expected_error in enumerate(expected_errors):
        assert str(expected_error) in str(errors.messages[i]), "Expected error '{}' not found in actual errors: {}".format(expected_error, errors.messages)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: closing parenthesis '}' does not match opening parenthesis '[' (line 27, col 149)
                'param2': [{'username': 'admin', 'password': 'mypassword'}, {'username': 'user', 'password': 'yourpassword', 'extra': 'unsupported'}}]
"""