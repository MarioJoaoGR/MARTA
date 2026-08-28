
import pytest
from ansible.cli.doc import DocCLI


def test_format_snippet_generates_yaml_snippet():
    doc = {
        'options': {
            'option1': {'description': 'This is option 1', 'type': 'str', 'required': True, 'default': None},
            'option2': {'description': 'This is option 2', 'type': 'int', 'required': False, 'default': 0}
        }
    }
    snippet = DocCLI.format_snippet('my_lookup_plugin', 'lookup', doc)
    assert "option1" in snippet
    assert "option2" in snippet
