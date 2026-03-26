
import pytest
from string_utils.manipulation import camel_case_to_snake
from string_utils.errors import InvalidInputError

def test_edge_case():
    # Test None input
    with pytest.raises(InvalidInputError):
        assert camel_case_to_snake(None) is None
