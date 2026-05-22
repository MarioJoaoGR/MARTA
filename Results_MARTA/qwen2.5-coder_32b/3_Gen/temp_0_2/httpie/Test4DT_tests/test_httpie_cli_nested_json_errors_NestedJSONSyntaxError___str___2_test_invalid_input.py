
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.nested_json.errors import NestedJSONSyntaxError

def test_invalid_input():
    with patch('httpie.cli.nested_json.errors.NestedJSONSyntaxError', autospec=True) as mock_error:
        source = "invalid json"
        token = MagicMock()
        message = "Invalid JSON structure"
        
        with pytest.raises(NestedJSONSyntaxError):
            raise NestedJSONSyntaxError(source, token, message)
