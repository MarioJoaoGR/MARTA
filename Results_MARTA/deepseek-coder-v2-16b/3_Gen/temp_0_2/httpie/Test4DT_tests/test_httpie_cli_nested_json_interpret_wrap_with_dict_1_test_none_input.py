
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.interpret import wrap_with_dict, NestedJSONArray

def test_none_input():
    with patch('httpie.cli.nested_json.interpret.EMPTY_STRING', ''):
        assert wrap_with_dict(None) == {}
