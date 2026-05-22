
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_utils import render_as_string, RenderableType

def test_none_input():
    with pytest.raises(TypeError):
        with patch('httpie.output.ui.rich_utils.Console') as mock_console:
            mock_console.side_effect = TypeError("renderable must be a rich object")
            render_as_string(None)
