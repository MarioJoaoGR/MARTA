
import pytest
from httpie.cli.nested_json.errors import NestedJSONSyntaxError

def test_valid_input():
    source = '{"key": [1, 2, {"innerKey": "value"}]}'
    
    with pytest.raises(NestedJSONSyntaxError) as exc_info:
        raise NestedJSONSyntaxError(source=source, token=None, message="Invalid nested structure detected.")
    
    assert str(exc_info.value) == 'HTTPie Syntax Error: Invalid nested structure detected.'
