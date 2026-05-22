
import pytest
from unittest.mock import patch
import pygments.styles

def get_available_styles():
    return sorted(BUNDLED_STYLES | set(pygments.styles.get_all_styles()))

# Assuming BUNDLED_STYLES is a predefined set of styles that are bundled with Pygments
BUNDLED_STYLES = {'default', 'friendly', 'monokai'}  # Example set, replace with actual values if known

@pytest.mark.parametrize("mocked_styles", [({'default', 'friendly', 'monokai'},), ({'solarized-dark', 'native'},)])
def test_valid_case(mocked_styles):
    with patch('pygments.styles.get_all_styles') as mock_get_all_styles:
        # Set up the mock to return a predefined set of styles
        mock_get_all_styles.return_value = list(mocked_styles[0])
        
        available_styles = get_available_styles()
        
        assert isinstance(available_styles, list)
        assert sorted(BUNDLED_STYLES | set(mocked_styles[0])) == available_styles
