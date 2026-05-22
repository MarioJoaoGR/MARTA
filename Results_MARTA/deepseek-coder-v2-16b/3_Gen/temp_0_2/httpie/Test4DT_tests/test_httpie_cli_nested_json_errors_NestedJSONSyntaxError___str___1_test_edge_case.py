
import pytest
from httpie.cli.nested_json.errors import NestedJSONSyntaxError

def test_edge_case():
    with pytest.raises(NestedJSONSyntaxError) as exc_info:
        raise NestedJSONSyntaxError("source", None, "Test message")
    
    assert str(exc_info.value) == 'HTTPie Syntax Error: Test message'
