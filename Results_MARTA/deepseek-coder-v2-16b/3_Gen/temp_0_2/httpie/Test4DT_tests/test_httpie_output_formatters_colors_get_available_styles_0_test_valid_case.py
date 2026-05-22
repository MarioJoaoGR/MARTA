
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import get_available_styles, BUNDLED_STYLES

def test_get_available_styles():
    # Mocking the necessary function to return a predefined list of styles
    with patch('httpie.output.formatters.colors.pygments.styles.get_all_styles') as mock_get_all_styles:
        mock_get_all_styles.return_value = ['monokai', 'default']  # Example styles
        
        available_styles = get_available_styles()
        
        assert isinstance(available_styles, list)
        assert sorted(BUNDLED_STYLES | {'monokai', 'default'}) == available_styles
