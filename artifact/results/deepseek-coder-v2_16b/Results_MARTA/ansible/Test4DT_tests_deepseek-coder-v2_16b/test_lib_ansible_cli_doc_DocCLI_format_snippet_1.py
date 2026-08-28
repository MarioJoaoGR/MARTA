
import pytest
from ansible.cli.doc import DocCLI


def test_invalid_input_plugin_type():
    with pytest.raises(AttributeError):
        DocCLI._format_snippet('my_plugin', 'invalid_type', {'options': {}})