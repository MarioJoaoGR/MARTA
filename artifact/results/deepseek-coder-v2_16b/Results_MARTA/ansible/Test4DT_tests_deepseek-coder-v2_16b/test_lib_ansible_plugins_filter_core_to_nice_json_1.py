
import pytest
from ansible.plugins.filter import core


def test_to_nice_json_with_indent():
    data = {'key': 'value'}
    result = core.to_nice_json(data, indent=2)
    assert isinstance(result, str), "Expected a string"
    assert result == '{\n  "key": "value"\n}', f"Unexpected result: {result}"

