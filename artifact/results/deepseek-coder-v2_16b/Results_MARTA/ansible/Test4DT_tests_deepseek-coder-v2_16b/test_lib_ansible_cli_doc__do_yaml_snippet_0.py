
import pytest
from ansible.cli.doc import _do_yaml_snippet

def test_valid_input_happy_path():
    doc = {
        'short_description': 'A short description of the task',
        'module': 'some_module',
        'options': {
            'option1': {'description': 'Description of option1', 'required': True},
            'option2': {'description': 'Description of option2', 'default': 'value'},
        }
    }
    expected = [
        "- name: A short description of the task",
        "  some_module:",
        "      option1: (required) # Description of option1",
        "      option2: value       # Description of option2"
    ]
    assert _do_yaml_snippet(doc) == expected

def test_edge_case_none():
    doc = None
    with pytest.raises(TypeError):
        _do_yaml_snippet(doc)

def test_invalid_input_error_handling():
    doc = {'short_description': 'A short description of the task', 'module': 123, 'options': {}}
    with pytest.raises(ValueError):
        _do_yaml_snippet(doc)
