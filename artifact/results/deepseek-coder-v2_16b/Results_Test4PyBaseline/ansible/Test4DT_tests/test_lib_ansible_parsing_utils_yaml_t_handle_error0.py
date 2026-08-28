
import pytest
from ansible.errors import AnsibleParserError
from ansible.parsing.utils.yaml import _handle_error
import yaml

# Simulate JSON and YAML exceptions for testing
json_exc = Exception("JSON parsing failed")
yaml_exc = yaml.YAMLError(yaml.scanner.ScannerError(None, None, "Invalid YAML syntax"))

def test__handle_error():
    with pytest.raises(AnsibleParserError) as excinfo:
        _handle_error(json_exc=json_exc, yaml_exc=yaml_exc, file_name='config.yaml', show_content=True)
    
    assert "We were unable to read either as JSON nor YAML" in str(excinfo.value)
    assert "JSON: JSON parsing failed" in str(excinfo.value)
    assert "Invalid YAML syntax" in str(excinfo.value)

def test__handle_error_no_problem_mark():
    # Test the case where yaml_exc does not have a problem mark
    yaml_exc_no_problem = yaml.YAMLError(yaml.scanner.ScannerError(None, None, "Invalid YAML syntax"))
    with pytest.raises(AnsibleParserError) as excinfo:
        _handle_error(json_exc=json_exc, yaml_exc=yaml_exc_no_problem, file_name='config.yaml', show_content=True)
    
    assert "We were unable to read either as JSON nor YAML" in str(excinfo.value)
    assert "JSON: JSON parsing failed" in str(excinfo.value)
    assert "Invalid YAML syntax" in str(excinfo.value)

def test__handle_error_show_content_false():
    with pytest.raises(AnsibleParserError) as excinfo:
        _handle_error(json_exc=json_exc, yaml_exc=yaml_exc, file_name='config.yaml', show_content=False)
    
    assert "We were unable to read either as JSON nor YAML" in str(excinfo.value)
    assert "JSON: JSON parsing failed" in str(excinfo.value)
    assert not "show_content is set to False, content will not be displayed." in str(excinfo.value)
