
import pytest
from string_utils.manipulation import reverse, InvalidInputError

def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        reverse(None)
