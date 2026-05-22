
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import get_available_styles, BUNDLED_STYLES

def test_get_available_styles():
    with patch('httpie.output.formatters.colors.BUNDLED_STYLES', {'test_style1', 'test_style2'}):
        with patch('httpie.output.formatters.colors.pygments.styles.get_all_styles') as mock_get_all_styles:
            mock_get_all_styles.return_value = ['user_defined_style']
            
            available_styles = get_available_styles()
            
            assert isinstance(available_styles, list)
            assert sorted(available_styles) == sorted({'test_style1', 'test_style2', 'user_defined_style'})
