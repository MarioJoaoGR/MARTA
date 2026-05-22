
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.nested_json.errors import NestedJSONSyntaxError

def test_invalid_inputs():
    with patch('httpie.cli.nested_json.errors.Token', autospec=True):
        with pytest.raises(NestedJSONSyntaxError) as exc_info:
            raise NestedJSONSyntaxError("source_code", None, "Invalid JSON structure")
    
    assert str(exc_info.value) == 'HTTPie Syntax Error: Invalid JSON structure'
