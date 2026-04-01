
from unittest import mock
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_edge_case():
    with pytest.raises(InvalidInputError):
        # Test case for edge case where input is not a string
        formatter = __StringFormatter(12345)  # Passing an integer instead of a string
