
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import get_available_styles, BUNDLED_STYLES

def test_get_available_styles():
    with patch('httpie.output.formatters.colors.pygments.styles.get_all_styles') as mock_get_all_styles:
        # Mock the return value of get_all_styles to simulate available styles
        mock_get_all_styles.return_value = ['mockstyle1', 'mockstyle2']
        
        # Call the function under test
        available_styles = get_available_styles()
        
        # Assert that the result is a sorted list containing both mocked and bundled styles
        assert isinstance(available_styles, list)
        assert set(available_styles) == BUNDLED_STYLES | {'mockstyle1', 'mockstyle2'}
        assert available_styles == sorted(BUNDLED_STYLES | {'mockstyle1', 'mockstyle2'})
