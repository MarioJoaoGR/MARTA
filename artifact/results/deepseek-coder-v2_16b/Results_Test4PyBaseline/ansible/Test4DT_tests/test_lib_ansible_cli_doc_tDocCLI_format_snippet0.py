# Module: ansible.cli.doc
import pytest
from ansible.cli.doc import DocCLI

# Test cases for the format_snippet function in the DocCLI class
def test_format_snippet_invalid_inventory():
    doc = {
        'options': {
            '_terms': ['arg1', 'arg2'],
            'option1': {'type': 'string', 'description': 'First option'},
            'option2': {'type': 'int', 'default': 0, 'description': 'Second option'}
        }
    }
    with pytest.raises(ValueError):
        DocCLI.format_snippet('example_plugin', 'inventory', doc)

def test_format_snippet_lookup():
    doc = {
        'options': {
            '_terms': ['arg1', 'arg2'],
            'option1': {'type': 'string', 'description': 'First option'},
            'option2': {'type': 'int', 'default': 0, 'description': 'Second option'}
        }
    }
    snippet = DocCLI.format_snippet('example_plugin', 'lookup', doc)
    assert isinstance(snippet, str), "Expected a string but got something else"
    # Add more assertions to check the content of the generated snippet if possible

def test_format_snippet_other_type():
    doc = {
        'options': {
            '_terms': ['arg1', 'arg2'],
            'option1': {'type': 'string', 'description': 'First option'},
            'option2': {'type': 'int', 'default': 0, 'description': 'Second option'}
        }
    }
    snippet = DocCLI.format_snippet('example_plugin', 'other_type', doc)
    assert isinstance(snippet, str), "Expected a string but got something else"
    # Add more assertions to check the content of the generated snippet if possible
