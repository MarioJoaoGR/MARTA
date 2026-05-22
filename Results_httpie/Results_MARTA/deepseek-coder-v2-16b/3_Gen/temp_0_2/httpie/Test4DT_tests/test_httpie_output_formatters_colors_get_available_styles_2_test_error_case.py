
import pytest
from unittest.mock import patch
import pygments.styles

def get_available_styles():
    return sorted(BUNDLED_STYLES | set(pygments.styles.get_all_styles()))

# Assuming BUNDLED_STYLES is a global variable or constant defined somewhere in the module
# If not, you might need to define it for this specific test case if it's used elsewhere.
BUNDLED_STYLES = set(["default", "friendly"])  # Example of what BUNDLED_STYLES might look like

@pytest.mark.parametrize("mocked_styles, expected", [
    (["solarized-dark"], ["default", "friendly", "solarized-dark"]),
    ([], ["default", "friendly"])
])
def test_error_case(mocked_styles, expected):
    with patch('pygments.styles.get_all_styles', return_value=mocked_styles):
        available_styles = get_available_styles()
        assert available_styles == expected
