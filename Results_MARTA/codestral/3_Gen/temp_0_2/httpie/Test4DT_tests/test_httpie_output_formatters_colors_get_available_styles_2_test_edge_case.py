
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import get_available_styles, BUNDLED_STYLES

def test_get_available_styles():
    with patch('httpie.output.formatters.colors.pygments.styles.get_all_styles') as mock_get_all_styles:
        # Mock the return value of get_all_styles to simulate a list of styles
        mock_get_all_styles.return_value = ['mocked_style1', 'mocked_style2']
        
        available_styles = get_available_styles()
        
        assert isinstance(available_styles, list)
        assert sorted(BUNDLED_STYLES | {'mocked_style1', 'mocked_style2'}) == available_styles
