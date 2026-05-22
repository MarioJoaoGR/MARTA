
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.nested_json.interpret import wrap_with_dict, NestedJSONArray

def test_valid_input():
    context = {'key': 'value'}
    
    with patch('httpie.cli.nested_json.interpret.NestedJSONArray', MagicMock()):
        result = wrap_with_dict(context)
        
        assert isinstance(result, dict)
        assert result == {'key': 'value'}
