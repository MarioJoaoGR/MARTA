
import pytest
from string_utils.manipulation import snake_case_to_camel, is_snake_case, InvalidInputError

def test_edge_cases():
    # Test None input
    with pytest.raises(InvalidInputError):
        assert snake_case_to_camel(None) == None
