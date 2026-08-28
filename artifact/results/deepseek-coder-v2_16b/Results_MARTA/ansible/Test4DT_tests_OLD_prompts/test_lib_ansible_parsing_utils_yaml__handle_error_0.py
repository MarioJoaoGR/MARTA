
import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleParserError
from ansible.parsing.utils.yaml import YAML_SYNTAX_ERROR, to_native
from ansible.parsing.utils.yaml import AnsibleBaseYAMLObject

def _handle_error(json_exc, yaml_exc, file_name='<string>', show_content=True):
    '''
    Handles errors that occur during the parsing of either JSON or YAML data. The function encapsulates information about the file name/position where a syntax error occurred in YAML and raises an `AnsibleParserError` to display detailed exception information.

    Parameters:
        json_exc (Exception): The exception raised while attempting to parse the input as JSON.
        yaml_exc (YAMLError): The specific YAML error that occurred during the parsing.
        file_name (str, optional): The name of the file from which the data was read. Defaults to '<string>'.
        show_content (bool, optional): Whether to include the content in the error message for display. Defaults to True.

    Raises:
        AnsibleParserError: An exception raised to encapsulate and display the syntax errors from both JSON and YAML parsers.
    '''
    err_obj = None
    if hasattr(yaml_exc, 'problem_mark'):
        err_obj = AnsibleBaseYAMLObject()
        err_obj.ansible_pos = (file_name, yaml_exc.problem_mark.line + 1, yaml_exc.problem_mark.column + 1)

    n_yaml_syntax_error = YAML_SYNTAX_ERROR % to_native(getattr(yaml_exc, 'problem', u''))
    n_err_msg = 'We were unable to read either as JSON nor YAML, these are the errors we got from each:\n' \
                'JSON: %s\n\n%s' % (to_native(json_exc), n_yaml_syntax_error)

    raise AnsibleParserError(n_err_msg, obj=err_obj, show_content=show_content, orig_exc=yaml_exc)

@patch('ansible.parsing.utils.yaml.getattr')
def test_valid_inputs(mock_getattr):
    json_exc = Exception("JSON Error")
    yaml_exc = MagicMock()
    yaml_exc.problem_mark = MagicMock()
    yaml_exc.problem_mark.line = 10
    yaml_exc.problem_mark.column = 20
    with pytest.raises(AnsibleParserError):
        _handle_error(json_exc, yaml_exc, file_name='test.yaml', show_content=True)

@patch('ansible.parsing.utils.yaml.getattr')
def test_invalid_inputs(mock_getattr):
    json_exc = Exception("JSON Error")
    yaml_exc = MagicMock()
    yaml_exc.problem_mark = MagicMock()
    yaml_exc.problem_mark.line = 10
    yaml_exc.problem_mark.column = 20
    with pytest.raises(AnsibleParserError):
        _handle_error(json_exc, yaml_exc, file_name='test.yaml', show_content=False)
