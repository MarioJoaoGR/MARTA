
import pytest
from unittest.mock import patch
from string_utils.manipulation import reverse, InvalidInputError

def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        assert reverse(None) is None
