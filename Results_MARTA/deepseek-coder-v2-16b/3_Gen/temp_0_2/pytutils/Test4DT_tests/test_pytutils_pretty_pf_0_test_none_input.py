
import pytest
from unittest.mock import patch, MagicMock
from pytutils.pretty import pf

@pytest.mark.parametrize("input_arg", [None])
def test_none_input(input_arg):
    with patch('pytutils.pretty.pygments', MagicMock()):
        # Mock the highlight method to return a specific value
        mock_highlight = MagicMock()
        mock_highlight.return_value = "formatted_output"
        pygments_mock = MagicMock()
        pygments_mock.highlight = mock_highlight
        
        with patch('pytutils.pretty.pygments', pygments_mock):
            result = pf(input_arg)
            assert result == "formatted_output"
