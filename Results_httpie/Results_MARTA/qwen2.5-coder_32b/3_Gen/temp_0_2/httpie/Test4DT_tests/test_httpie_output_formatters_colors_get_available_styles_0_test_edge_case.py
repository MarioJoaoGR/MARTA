
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import get_available_styles, BUNDLED_STYLES

def test_get_available_styles():
    with patch('httpie.output.formatters.colors.BUNDLED_STYLES', {'solarized-dark', 'monokai'}):
        with patch('httpie.output.formatters.colors.pygments.styles.get_all_styles') as mock_get_all_styles:
            # Mock the return value of get_all_styles to simulate available styles
            mock_get_all_styles.return_value = ['solarized-dark', 'monokai', 'default']
            
            available_styles = get_available_styles()
            assert isinstance(available_styles, list)
            assert set(available_styles) == {'solarized-dark', 'monokai', 'default'}
            assert sorted(available_styles) == ['default', 'monokai', 'solarized-dark']
