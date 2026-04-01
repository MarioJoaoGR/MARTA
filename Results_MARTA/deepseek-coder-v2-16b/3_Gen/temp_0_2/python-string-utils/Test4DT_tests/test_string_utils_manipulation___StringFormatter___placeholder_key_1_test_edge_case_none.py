
from string_utils.manipulation import __StringFormatter, InvalidInputError
from unittest.mock import patch
import pytest

def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        # Test case where input is None
        formatter = __StringFormatter(None)
