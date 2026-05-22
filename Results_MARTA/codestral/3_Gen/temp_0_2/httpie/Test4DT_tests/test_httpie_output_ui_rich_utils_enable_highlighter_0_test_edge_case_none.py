
from httpie.output.ui.rich_utils import enable_highlighter
from unittest.mock import patch, MagicMock
import pytest

@pytest.fixture
def mock_console():
    console = MagicMock()
    yield console

@pytest.fixture
def mock_highlighter():
    highlighter = MagicMock()
    yield highlighter

def test_edge_case_none(mock_console, mock_highlighter):
    with patch('httpie.output.ui.rich_utils.Console', return_value=mock_console):
        with enable_highlighter(mock_console, mock_highlighter) as enhanced_console:
            assert enhanced_console == mock_console
            assert enhanced_console.highlighter == mock_highlighter
