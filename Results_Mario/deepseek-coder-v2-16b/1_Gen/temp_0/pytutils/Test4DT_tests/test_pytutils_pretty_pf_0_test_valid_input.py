
import pytest
from unittest.mock import patch
from pytutils.pretty import pf

@pytest.mark.skip(reason="This test is disabled because it requires Pygments to be installed and properly configured in the environment.")
def test_valid_input():
    # Test with valid input, should return highlighted code if Pygments is available
    with patch('pytutils.pretty.pygments', autospec=True):
        result = pf([1, 2, {'key': 'value'}])
        assert isinstance(result, str), "Expected a string representation"
